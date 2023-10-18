# target
* object website: https://weixin.sogou.com/weixin?ie=utf8&s_from=input&_sug_=y&_sug_type_=&type=2&query=%E9%A3%8E%E6%99%AF
* 任务：抓取详情页标题，时间，文章，图片
* 需求，每个文章一个文件夹，当中存储文章内容，文章图片

# 


* python访问详情页网址会转到验证网址，浏览器访问不会转到验证网址
* python中在headers添加~~本来会自动生成的cookie~~，python默认的cookie会被识别，添加好抓包得到的，会返回：
* 
<meta content="always" name="referrer">
<script>

    (new Image()).src = 'https://weixin.sogou.com/approve?uuid=' + '1b12fcf9-59b1-4953-9c06-b9144978bba7' + '&token=' + '7B66C8C7187A6F7E646263BB8188A47E65B2F0DC652DFE8E' + '&from=inner';

    setTimeout(function () {
        var url = '';
        url += 'http://mp.w';
        url += 'eixin.qq.co';
        url += 'm/s?src=11&';
        url += 'timestamp=1';
        url += '697512486&v';
        url += 'er=4839&sig';
        url += 'nature=o9P1';
        url += 'Aqr1cvTYiSd';
        url += 'hxzyzuDBudI';
        url += '*sQYnw9US2N';
        url += 'XddKFn*tpdoaHsSlZEXSiaT6XLWwyNj0V5irNBHVQYULoHUSt-**zuHEj1QP10CmHy1*ps38339XRIQi8PGUV56k76m&new=1';
        url.replace("@", "");
        window.location.replace(url)
    },100);

</script>

* 用以上的文本拼接出要跳转的url，然后设置好请求头就可以获取详情页数据了
* 详情页会检测cookie，频繁访问会封cookie