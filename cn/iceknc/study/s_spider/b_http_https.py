# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/7/23
# @Desc  : 
"""
常用的请求报头
    1. Host (主机和端口号)
        Host：对应网址URL中的Web名称和端口号，用于指定被请求资源的Internet主机和端口号，
              通常属于URL的一部分。
    2. Connection (链接类型)
        Connection：表示客户端与服务连接类型
        Client 发起一个包含 Connection:keep-alive 的请求，HTTP/1.1使用 keep-alive 为默认值。
        Server收到请求后：
            如果 Server 支持 keep-alive，回复一个包含 Connection:keep-alive 的响应，不关闭连接；
            如果 Server 不支持 keep-alive，回复一个包含 Connection:close 的响应，关闭连接。
        如果client收到包含 Connection:keep-alive 的响应，向同一个连接发送下一个请求，直到一方主动关闭连接。
        keep-alive在很多情况下能够重用连接，减少资源消耗，缩短响应时间，比如当浏览器需要多个文件时(比如一个HTML文件和
        相关的图形文件)，不需要每次都去请求建立连接。
    3. Upgrade-Insecure-Requests (升级为HTTPS请求)
        Upgrade-Insecure-Requests：升级不安全的请求，意思是会在加载 http 资源时自动替换成 https 请求，
        让浏览器不再显示https页面中的http请求警报。
        HTTPS 是以安全为目标的 HTTP 通道，所以在 HTTPS 承载的页面上不允许出现 HTTP 请求，一旦出现就是提示或报错。
    4. User-Agent (浏览器名称)
        User-Agent：是客户浏览器的名称
    5. Accept (传输文件类型)
        Accept：指浏览器或其他客户端可以接受的MIME（Multipurpose Internet Mail Extensions
        （多用途互联网邮件扩展））文件类型，服务器可以根据它判断并返回适当的文件格式。
        举例：
            Accept: */*：表示什么都可以接收。
            Accept：image/gif：表明客户端希望接受GIF图像格式的资源；
            Accept：text/html：表明客户端希望接受html文本。
            Accept: text/html, application/xhtml+xml;q=0.9, image/*;q=0.8：表示浏览器支持的
            MIME 类型分别是 html文本、xhtml和xml文档、所有的图像格式资源。
                q是权重系数，范围 0 =< q <= 1，q 值越大，请求越倾向于获得其“;”之前的类型表示的内容。
                若没有指定q值，则默认为1，按从左到右排序顺序；若被赋值为0，则用于表示浏览器不接受此内容类型。
            Text：用于标准化地表示的文本信息，文本消息可以是多种字符集和或者多种格式的
            Application：用于传输应用程序数据或者二进制数据
    6. Referer (页面跳转处)
        Referer：表明产生请求的网页来自于哪个URL，用户是从该 Referer页面访问到当前请求的页面。
        这个属性可以用来跟踪Web请求来自哪个页面，是从什么网站来的等。
        有时候遇到下载某网站图片，需要对应的referer，否则无法下载图片，那是因为人家做了防盗链，
        原理就是根据referer去判断是否是本网站的地址，如果不是，则拒绝，如果是，就可以下载
    7. Accept-Encoding（文件编解码格式）
        Accept-Encoding：指出浏览器可以接受的编码方式。编码方式不同于文件格式，它是为了压缩文件并加速文件
        传递速度。浏览器在接收到Web响应之后先解码，然后再检查文件格式，许多情形下这可以减少大量的下载时间。
        举例：Accept-Encoding:gzip;q=1.0, identity; q=0.5, *;q=0
        如果有多个Encoding同时匹配, 按照q值顺序排列，本例中按顺序支持 gzip, identity压缩编码，
        支持gzip的浏览器会返回经过gzip编码的HTML页面。 如果请求消息中没有设置这个域服务器假定客户端
        对各种内容编码都可以接受。
    8. Accept-Language（语言种类）
        Accept-Langeuage：指出浏览器可以接受的语言种类，如en或en-us指英语，zh或者zh-cn指中文，
        当服务器能够提供一种以上的语言版本时要用到。
    9. Accept-Charset（字符编码）
        Accept-Charset：指出浏览器可以接受的字符编码。
        举例：Accept-Charset:iso-8859-1,gb2312,utf-8
        ISO8859-1：通常叫做Latin-1。Latin-1包括了书写所有西方欧洲语言不可缺少的附加字符，
        英文浏览器的默认值是ISO-8859-1.
        gb2312：标准简体中文字符集;
        utf-8：UNICODE 的一种变长字符编码，可以解决多种语言文本显示问题，从而实现应用国际化和本地化。
        如果在请求消息中没有设置这个域，缺省是任何字符集都可以接受
    10. Cookie （Cookie）
        Cookie：浏览器用这个属性向服务器发送Cookie。Cookie是在浏览器中寄存的小型数据体，
        它可以记载和服务器相关的用户信息，也可以用来实现会话功能，以后会详细讲。
    11. Content-Type (POST数据类型)
        Content-Type：POST请求里用来表示的内容类型。
        举例：Content-Type = Text/XML; charset=gb2312：
        指明该请求的消息体中包含的是纯文本的XML类型的数据，字符编码采用“gb2312”。

常用的响应报头
    1. Cache-Control：must-revalidate, no-cache, private。
        这个值告诉客户端，服务端不希望客户端缓存资源，在下次请求资源时，必须要从新请求服务器，
        不能从缓存副本中获取资源。
        Cache-Control是响应头中很重要的信息，当客户端请求头中包含Cache-Control:max-age=0请求，
        明确表示不会缓存服务器资源时,Cache-Control作为作为回应信息，通常会返回no-cache，
        意思就是说，"那就不缓存呗"。
        当客户端在请求头中没有包含Cache-Control时，服务端往往会定,不同的资源不同的缓存策略，
        比如说oschina在缓存图片资源的策略就是Cache-Control：max-age=86400,这个意思是，从当前时间开始，
        在86400秒的时间内，客户端可以直接从缓存副本中读取资源，而不需要向服务器请求。
    2. Connection：keep-alive
        这个字段作为回应客户端的Connection：keep-alive，告诉客户端服务器的tcp连接也是一个长连接，
        客户端可以继续使用这个tcp连接发送http请求。
    3. Content-Encoding:gzip
        告诉客户端，服务端发送的资源是采用gzip编码的，客户端看到这个信息后，应该采用gzip对资源进行解码。
    4. Content-Type：text/html;charset=UTF-8
        告诉客户端，资源文件的类型，还有字符编码，客户端通过utf-8对资源进行解码，然后对资源进行html解析。
        通常我们会看到有些网站是乱码的，往往就是服务器端没有返回正确的编码。
    5. Date：Sun, 21 Sep 2016 06:18:21 GMT
        这个是服务端发送资源时的服务器时间，GMT是格林尼治所在地的标准时间。http协议中发送的时间都是GMT的，
        这主要是解决在互联网上，不同时区在相互请求资源的时候，时间混乱问题。
    6. Expires:Sun, 1 Jan 2000 01:00:00 GMT
        这个响应头也是跟缓存有关的，告诉客户端在这个时间前，可以直接访问缓存副本，很显然这个值会存在问题，
        因为客户端和服务器的时间不一定会都是相同的，如果时间不同就会导致问题。
        所以这个响应头是没有Cache-Control：max-age=*这个响应头准确的，因为max-age=date中的date是个
        相对时间，不仅更好理解，也更准确。
    7. Pragma:no-cache
        这个含义与Cache-Control等同。
    8.Server：Tengine/1.4.6
        这个是服务器和相对应的版本，只是告诉客户端服务器的信息。
    9. Transfer-Encoding：chunked
        这个响应头告诉客户端，服务器发送的资源的方式是分块发送的。一般分块发送的资源都是服务器动态生成的，
        在发送时还不知道发送资源的大小，所以采用分块发送，每一块都是独立的，独立的块都能标示自己的长度，
        最后一块是0长度的，当客户端读到这个0长度的块时，就可以确定资源已经传输完了。
    10. Vary: Accept-Encoding
        告诉缓存服务器，缓存压缩文件和非压缩文件两个版本，现在这个字段用处并不大，因为现在的浏览器都是支持压缩的。

Cookie 和 Session：
    服务器和客户端的交互仅限于请求/响应过程，结束之后便断开，在下一次请求时，服务器会认为新的客户端。
    为了维护他们之间的链接，让服务器知道这是前一个用户发送的请求，必须在一个地方保存客户端的信息。
    Cookie：通过在 客户端 记录的信息确定用户的身份。
    Session：通过在 服务器端 记录的信息确定用户的身份

响应状态码
    响应状态代码有三位数字组成，第一个数字定义了响应的类别，且有五种可能取值。
    常见状态码：
        100~199：表示服务器成功接收部分请求，要求客户端继续提交其余请求才能完成整个处理过程。
        200~299：表示服务器成功接收请求并已完成整个处理过程。常用200（OK 请求成功）。
        300~399：为完成请求，客户需进一步细化请求。例如：请求的资源已经移动一个新地址、
                 常用302（所请求的页面已经临时转移至新的url）、307和304（使用缓存资源）。
        400~499：客户端的请求有错误，常用404（服务器无法找到被请求的页面）、403（服务器拒绝访问，权限不够）。
        500~599：服务器端出现错误，常用500（请求未完成。服务器遇到不可预知的情况）。

HTTP响应状态码参考
    1xx:信息
        100 Continue
            服务器仅接收到部分请求，但是一旦服务器并没有拒绝该请求，客户端应该继续发送其余的请求。
        101 Switching Protocols
            服务器转换协议：服务器将遵从客户的请求转换到另外一种协议。

    2xx:成功
        200 OK
            请求成功（其后是对GET和POST请求的应答文档）
        201 Created
            请求被创建完成，同时新的资源被创建。
        202 Accepted
            供处理的请求已被接受，但是处理未完成。
        203 Non-authoritative Information
            文档已经正常地返回，但一些应答头可能不正确，因为使用的是文档的拷贝。
        204 No Content
            没有新文档。浏览器应该继续显示原来的文档。如果用户定期地刷新页面，而Servlet可以确定用户文档足够新，这个状态代码是很有用的。
        205 Reset Content
            没有新文档。但浏览器应该重置它所显示的内容。用来强制浏览器清除表单输入内容。
        206 Partial Content
            客户发送了一个带有Range头的GET请求，服务器完成了它。

    3xx:重定向
        300 Multiple Choices
            多重选择。链接列表。用户可以选择某链接到达目的地。最多允许五个地址。
        301 Moved Permanently
            所请求的页面已经转移至新的url。
        302 Moved Temporarily
            所请求的页面已经临时转移至新的url。
        303 See Other
            所请求的页面可在别的url下被找到。
        304 Not Modified
            未按预期修改文档。客户端有缓冲的文档并发出了一个条件性的请求（一般是提供If-Modified-Since头表示客户只想比指定日期更新的文档）。
            服务器告诉客户，原来缓冲的文档还可以继续使用。
        305 Use Proxy
            客户请求的文档应该通过Location头所指明的代理服务器提取。
        306 Unused
            此代码被用于前一版本。目前已不再使用，但是代码依然被保留。
        307 Temporary Redirect
            被请求的页面已经临时移至新的url。

    4xx:客户端错误
        400 Bad Request
            服务器未能理解请求。
        401 Unauthorized
            被请求的页面需要用户名和密码。
        401.1
            登录失败。
        401.2
            服务器配置导致登录失败。
        401.3
            由于 ACL 对资源的限制而未获得授权。
        401.4
            筛选器授权失败。
        401.5
            ISAPI/CGI 应用程序授权失败。
        401.7
            访问被 Web 服务器上的 URL 授权策略拒绝。这个错误代码为 IIS 6.0 所专用。
        402 Payment Required
            此代码尚无法使用。
        403 Forbidden
            对被请求页面的访问被禁止。
        403.1
            执行访问被禁止。
        403.2
            读访问被禁止。
        403.3
            写访问被禁止。
        403.4
            要求 SSL。
        403.5
            要求 SSL 128。
        403.6
            IP 地址被拒绝。
        403.7
            要求客户端证书。
        403.8
            站点访问被拒绝。
        403.9
            用户数过多。
        403.10
            配置无效。
        403.11
            密码更改。
        403.12
            拒绝访问映射表。
        403.13
            客户端证书被吊销。
        403.14
            拒绝目录列表。
        403.15
            超出客户端访问许可。
        403.16
            客户端证书不受信任或无效。
        403.17
            客户端证书已过期或尚未生效。
        403.18
            在当前的应用程序池中不能执行所请求的 URL。这个错误代码为 IIS 6.0 所专用。
        403.19
            不能为这个应用程序池中的客户端执行 CGI。这个错误代码为 IIS 6.0 所专用。
        403.20
            Passport 登录失败。这个错误代码为 IIS 6.0 所专用。
        404 Not Found
            服务器无法找到被请求的页面。
        404.0
            没有找到文件或目录。
        404.1
            无法在所请求的端口上访问 Web 站点。
        404.2
            Web 服务扩展锁定策略阻止本请求。
        404.3
            MIME 映射策略阻止本请求。
        405 Method Not Allowed
            请求中指定的方法不被允许。
        406 Not Acceptable
            服务器生成的响应无法被客户端所接受。
        407 Proxy Authentication Required
            用户必须首先使用代理服务器进行验证，这样请求才会被处理。
        408 Request Timeout
            请求超出了服务器的等待时间。
        409 Conflict
            由于冲突，请求无法被完成。
        410 Gone
            被请求的页面不可用。
        411 Length Required
            "Content-Length" 未被定义。如果无此内容，服务器不会接受请求。
        412 Precondition Failed
            请求中的前提条件被服务器评估为失败。
        413 Request Entity Too Large
            由于所请求的实体的太大，服务器不会接受请求。
        414 Request-url Too Long
            由于url太长，服务器不会接受请求。当post请求被转换为带有很长的查询信息的get请求时，就会发生这种情况。
        415 Unsupported Media Type
            由于媒介类型不被支持，服务器不会接受请求。
        416 Requested Range Not Satisfiable
            服务器不能满足客户在请求中指定的Range头。
        417 Expectation Failed
            执行失败。
        423
            锁定的错误。

    5xx:服务器错误
        500 Internal Server Error
            请求未完成。服务器遇到不可预知的情况。
        500.12
            应用程序正忙于在 Web 服务器上重新启动。
        500.13
            Web 服务器太忙。
        500.15
            不允许直接请求 Global.asa。
        500.16
            UNC 授权凭据不正确。这个错误代码为 IIS 6.0 所专用。
        500.18
            URL 授权存储不能打开。这个错误代码为 IIS 6.0 所专用。
        500.100
            内部 ASP 错误。
        501 Not Implemented
            请求未完成。服务器不支持所请求的功能。
        502 Bad Gateway
            请求未完成。服务器从上游服务器收到一个无效的响应。
        502.1
            CGI 应用程序超时。　·
        502.2
            CGI 应用程序出错。
        503 Service Unavailable
            请求未完成。服务器临时过载或当机。
        504 Gateway Timeout
            网关超时。
        505 HTTP Version Not Supported
            服务器不支持请求中指明的HTTP协议版本
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






