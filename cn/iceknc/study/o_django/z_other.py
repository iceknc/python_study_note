# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/10
# @Desc  : 
"""
富文本编辑器
    借助富文本编辑器，网站的编辑人员能够像使用offfice一样编写出漂亮的、所见即所得的页面。此处以tinymce为例，其它富文本编辑器的使用也是类似的。
        在虚拟环境中安装包。
            pip install django-tinymce==2.6.0
        安装完成后，可以使用在Admin管理中，也可以自定义表单使用。
        在<项目名>/settings.py中为INSTALLED_APPS添加编辑器应用。
            INSTALLED_APPS = (
                ...
                'tinymce',
            )
        在<项目名>/settings.py中添加编辑器配置。
            TINYMCE_DEFAULT_CONFIG = {
                'theme': 'advanced',
                'width': 600,
                'height': 400,
            }
        在<项目名>/urls.py中配置编辑器url。
            urlpatterns = [
                ...
                url(r'^tinymce/', include('tinymce.urls')),
            ]
        定义模型的属性为HTMLField()类型
            from tinymce.models import HTMLField
    自定义使用
        在<应用名>/views.py中定义视图editor，用于显示编辑器。
            def editor(request):
                return render(request, 'test_app/editor.html')
        在<应用名>/urls.py中配置url。
            url(r'^editor/',views.editor),
        拷贝tiny_mce_src.js文件、langs文件夹以及themes文件夹拷贝到项目目录下的static/js/目录下
            ../site-packages/tinymce/static/tiny_mce
    显示
        通过富文本编辑器产生的字符串是包含html的。在模板中显示字符串时，默认会进行html转义，如果想正常显示需要关闭转义:
            方式一：过滤器safe
            方式二：标签autoescape off

全文检索
    全文检索不同于特定字段的模糊查询，使用全文检索的效率更高，并且能够对于中文进行分词处理。
        haystack：全文检索的框架，支持whoosh、solr、Xapian、Elasticsearc四种全文检索引擎。
        whoosh：纯Python编写的全文搜索引擎，虽然性能比不上sphinx、xapian、Elasticsearc等，但是无二进制包，
        程序不会莫名其妙的崩溃，对于小型的站点，whoosh已经足够使用。
        jieba：一款免费的中文分词包，如果觉得不好用可以使用一些收费产品。
    在虚拟环境中依次安装需要的包
        pip install django-haystack
        pip install whoosh
        pip install jieba
    在<项目名>/settings.py中为INSTALLED_APPS添加编辑器应用。
            INSTALLED_APPS = (
                ...
                'haystack',
            )
    在<项目名>/settings.py文件中配置搜索引擎。
        HAYSTACK_CONNECTIONS = {
            'default': {
                #使用whoosh引擎
                'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
                #索引文件路径
                'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
            }
        }
        #当添加、修改、删除数据时，自动生成索引
        HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
    在<项目名>/urls.py中添加搜索的配置。
        url(r'^search/', include('haystack.urls')),
    创建引擎及索引
        在<应用名>目录下创建search_indexes.py文件。
            from haystack import indexes
            from booktest.models import GoodsInfo
            #指定对于某个类的某些数据建立索引
            class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
                text = indexes.CharField(document=True, use_template=True)

                def get_model(self):
                    return GoodsInfo

                def index_queryset(self, using=None):
                    return self.get_model().objects.all()
    在templates目录下创建"search/indexes/<应用名>/"目录,创建"goodsinfo_text.txt"文件
        #指定索引的属性
        {{object.content}}
    找到虚拟环境下的haystack目录../site-packages/haystack/backends/创建ChineseAnalyzer.py文件
        import jieba
        from whoosh.analysis import Tokenizer, Token

        class ChineseTokenizer(Tokenizer):
            def __call__(self, value, positions=False, chars=False,keeporiginal=False, removestops=True,
                start_pos=0, start_char=0, mode='', **kwargs):
                t = Token(positions, chars, removestops=removestops, mode=mode,**kwargs)
                seglist = jieba.cut(value, cut_all=True)
                for w in seglist:
                    t.original = t.text = w
                    t.boost = 1.0
                    if positions:
                        t.pos = start_pos + value.find(w)
                    if chars:
                        t.startchar = start_char + value.find(w)
                        t.endchar = start_char + value.find(w) + len(w)
                    yield t

            def ChineseAnalyzer():
                return ChineseTokenizer()
    复制whoosh_backend.py文件，改名：whoosh_cn_backend.py
    打开复制出来的新文件，引入中文分析类，内部采用jieba分词。
        from .ChineseAnalyzer import ChineseAnalyzer
        查找 analyzer=StemmingAnalyzer()
        改为 analyzer=ChineseAnalyzer()
    初始化索引数据 python manage.py rebuild_index
    使用
        <form method='get' action="/search/" target="_blank">
            <input type="text" name="q">
            <br>
            <input type="submit" value="查询">
        </form>
    自定义搜索结果模板：在templates/search/目录下创建search.html。
        搜索结果进行分页，视图向模板中传递的上下文如下：
            query：搜索关键字
            page：当前页的page对象
            paginator：分页paginator对象

        <h1>搜索&nbsp;<b>{{query}}</b>&nbsp;结果如下：</h1>
        <ul>
        {%for item in page%}
            <li>{{item.object.id}}--{{item.object.content|safe}}</li>
        {%empty%}
        <li>啥也没找到</li>
        {%endfor%}
        </ul>
        <hr>
        {%for pindex in page.paginator.page_range%}
            {%if pindex == page.number%}
                {{pindex}}&nbsp;&nbsp;
            {%else%}
                <a href="?q={{query}}&amp;page={{pindex}}">{{pindex}}</a>&nbsp;&nbsp;
            {%endif%}
        {%endfor%}

"""

def main():
    pass


if __name__ == "__main__":
    main()
    






