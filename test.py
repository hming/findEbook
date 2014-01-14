# -*- coding:UTF-8 -*-
import re

s = '''


﻿﻿<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link href="./css/style.css" rel="stylesheet" type="text/css" />
    <title>亲子·教育 - epub电子书</title>
    <meta name="keywords" content="epub电子书,电子书下载,免费电子书,ibook电子书,ipad电子书,免费ibook" />
	<meta name="description" content="免费电子书分享平台,免费在线电子书阅读,发布平台,提供免费电子书下载等服务." />
</head>

<body id="wapper">
﻿<div id="h_container">
  <div id="header" style="margin-bottom:10px;">
<div id="logo" style="width:600px; float:left"><span class="in" style="margin-left:5px;"><a href="/index.php">首页</a></span><span class="in"><a href="/en_feature.php">英文书籍</a></span><span class="in"><a href="/all_txt.php">最新上传书籍</a></span> <span class="in"><a href="/publish.php">博客出书</a></span> <span class="in"><a href="/bbs.php">讨论区</a></span></div>

    	<div class="top_right">
               m221221 <!-- <span style="margin-left:8px;"><a href="favorite.php">收藏的书籍</a></span> --> <!-- <span style="margin-left:8px;"><a href="download.php">下载的书籍</a></span>--><span style="margin-left:8px;"><a href="my_txt_books.php">制作的书籍</a></span> <span style="margin-left:8px;"><a href="logout.php">退出</a></span>
                </div>
        <div style="clear:both"></div>
  </div>
</div>

        <div>
          <table width="100%" border="0">
            <tr>
              <td width="140"><a href="index.php"><img src="/images/logo.jpg" align="absmiddle" /></a></br></br></td>
              <td><form action="/search.php" method="get" class="searchform">
                 <p class="searchkey">
                    <input type="text" tabindex="1" class="txt" value="" maxlength="33" size="60" name="q" id="srchtxt1">
                    <input type="submit" class="btn" value="搜索" />
                <span style="margin-left:30px; font-size:14px;"><a href="/txt2epub.php" title="TXT转ePub"><b>TXT转ePub</b></a></span><span style="margin-left:20px; font-size:14px;"><a href="/make_books.php" title="制作电子书">制作电子书</a></span><span style="margin-left:20px; font-size:14px;"><a href="/post.php?upload=1">上传ePub</a></span>
                </p>
             </form>   </td>
            </tr>
          </table>
        </div>


</div>



<div style=" background:#FFF6EE; padding:10px; font-size:14px; margin:0px 0 5px 0">
	本站严禁涉及淫秽、色情、反动等非法内容！一旦发现，立即封账号！欢迎举报！举报邮箱：coaybook@163.com
	</div>
<!--	<a href="http://itunes.apple.com/cn/app/coay-shu-cheng/id557502085?mt=8" target="_blank"><img src="logo3.gif"/></a> -->

  <div id="container">
      <div id="left">
      	<h2 style="border-bottom:1px solid #006600; padding-bottom:5px;">亲子·教育</h2>
                    <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=366860" title="窗边的小豆豆"><img src="http://www.coay.com/upload_cover/s/1388584564.jpg" height="100" alt="窗边的小豆豆" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=366860">窗边的小豆豆</a></div>
                    <div class="author">日黑柳彻子</div>
                    <div class="des">
                    	《窗边的小豆豆》讲述了作者上小学时的一段真实的故事：小豆豆因淘气被原学校退学后，来到巴学园。小林校长却常常对小豆豆说：“你真是一个好孩子呀！”在小林校长的爱护和引导下，一般人眼里“怪怪”的小豆豆逐渐变成了一个大家都能接受的孩子。巴学园里随和、亲切的教学方式使这里的孩子们度过了人生最美好的时光。这本书不仅带给全世界几千万读者无数的感动和笑声，而且为现代教育的发展注入了新的活力，成为20世纪全球最有影响的作品之一。                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=366385" title="精灵1"><img src="http://www.coay.com/upload_cover/s/1387921829.jpg" height="100" alt="精灵1" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=366385">精灵1</a></div>
                    <div class="author">A</div>
                    <div class="des">
                    	SA                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=366135" title="忘记忘记"><img src="http://www.coay.com/upload_cover/s/1387570630.jpg" height="100" alt="忘记忘记" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=366135">忘记忘记</a></div>
                    <div class="author">v</div>
                    <div class="des">
                    	a                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=366098" title="Charlotte's Web"><img src="http://www.coay.com/upload_cover/s/1387544447.jpg" height="100" alt="Charlotte's Web" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=366098">Charlotte's Web</a></div>
                    <div class="author">E.  B.  White</div>
                    <div class="des">


Charlotte's Web
By
E.  B.  White
Copyright 1952
Contents
1.	BEFORE BREAKFAST
2.	WILBUR
3.	ESCAPE
4.	Loneliness
5.	CHARLLOTTE
6.	SUMMER DAYS
7.	BAD NEWS
8.	 A TALK AT HOME
9.	WILBUR'S BOAST
10.	AN EXPLOSION
11.	THE MIRACLE
12.	A MEETI                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=365773" title="我们仨"><img src="http://www.coay.com/upload_cover/s/1387052918.jpg" height="100" alt="我们仨" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=365773">我们仨</a></div>
                    <div class="author"></div>
                    <div class="des">
                    	我们仨                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=365019" title="外公是棵樱桃树"><img src="http://www.coay.com/upload_cover/s/1386113015.jpg" height="100" alt="外公是棵樱桃树" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=365019">外公是棵樱桃树</a></div>
                    <div class="author">安琪拉·那涅第</div>
                    <div class="des">
                    	这样的一本好书，字里行间焕发的亲情，就像一颗颗的樱桃，甜蜜多汁呀！                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=365018" title="外公是棵樱桃树"><img src="http://www.coay.com/upload_cover/s/1386111479.jpg" height="100" alt="外公是棵樱桃树" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=365018">外公是棵樱桃树</a></div>
                    <div class="author">安琪拉·那涅第</div>
                    <div class="des">
                    	这样的一本好书，字里行间焕发的亲情，就像一颗颗的樱桃，甜蜜多汁呀！                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=363575" title="英语翻译"><img src="http://www.coay.com/images/s_cover.jpg" height="100" alt="英语翻译" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=363575">英语翻译</a></div>
                    <div class="author">123</div>
                    <div class="des">
                    	2313213213211321                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=363568" title="天才宝宝：爹地，我是妈咪偷来的"><img src="http://www.coay.com/upload_cover/s/1383769951.jpg" height="100" alt="天才宝宝：爹地，我是妈咪偷来的" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=363568">天才宝宝：爹地，我是妈咪偷来的</a></div>
                    <div class="author"></div>
                    <div class="des">
                    	天才宝宝：爹地，我是妈咪偷来的                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=363103" title="安徒生童话"><img src="http://www.coay.com/upload_cover/s/1383194146.jpg" height="100" alt="安徒生童话" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=363103">安徒生童话</a></div>
                    <div class="author"></div>
                    <div class="des">
                    	安徒生童话                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=362050" title="GL02"><img src="http://www.coay.com/upload_cover/s/1382084717.jpg" height="100" alt="GL02" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=362050">GL02</a></div>
                    <div class="author"></div>
                    <div class="des">
                    	fasdfdfddfdsa                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=361425" title="friends"><img src="http://www.coay.com/upload_cover/s/1381426699.jpg" height="100" alt="friends" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=361425">friends</a></div>
                    <div class="author">noman</div>
                    <div class="des">
                    	talk about friends                     </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=361417" title="捕捉儿童敏感期"><img src="http://www.coay.com/upload_cover/s/1381420479.jpg" height="100" alt="捕捉儿童敏感期" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=361417">捕捉儿童敏感期</a></div>
                    <div class="author">蒙特梭利</div>
                    <div class="des">
                    	多少父母知道，婴儿刚出生时喜欢看黑白相界的地方，而不是人们通常认为的彩球？婴幼儿喝了糖水后为什么拒绝再喝白水？他为什么爱吃手？还对非常微小的东西感兴趣？他为什么不断扔掉手里的东西，你捡起来递给他，他会再扔掉？让他听磁带，他的兴趣为什么不在听上，而是在来回装卸磁带上。。。。。。
　　这一切，揭示的是儿童生命过程中的一个秘密——敏感期。
　　所谓敏感期，是指在0——6岁的成长过程中，儿童受内在生命力的驱使，在某个时间段内，专心吸收环境中某一事物的特质，并不断重复实践的过程。顺利通过一个敏感期后，儿童的心智                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=360157" title="爱弥儿"><img src="http://www.coay.com/upload_cover/s/1380258592.jpg" height="100" alt="爱弥儿" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=360157">爱弥儿</a></div>
                    <div class="author">卢梭</div>
                    <div class="des">
                    	法国思想家卢梭的教育名著                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=359995" title="计算"><img src="http://www.coay.com/upload_cover/s/1379839273.jpg" height="100" alt="计算" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=359995">计算</a></div>
                    <div class="author"></div>
                    <div class="des">
                    	计算计算计算计算计算计算计算计算计算                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=359994" title="判断"><img src="http://www.coay.com/upload_cover/s/1379839210.jpg" height="100" alt="判断" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=359994">判断</a></div>
                    <div class="author"></div>
                    <div class="des">
                    	判断判断判断判断判断判断判断判断判断判断                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=359993" title="多选"><img src="http://www.coay.com/upload_cover/s/1379839088.jpg" height="100" alt="多选" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=359993">多选</a></div>
                    <div class="author">噢噢</div>
                    <div class="des">
                    	考试单选考试单选考试单选考试单选考试单选考试单选考试单选考试单选                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=359992" title="考试单选"><img src="http://www.coay.com/upload_cover/s/1379838858.jpg" height="100" alt="考试单选" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=359992">考试单选</a></div>
                    <div class="author"></div>
                    <div class="des">
                    	考试单选考试单选考试单选考试单选考试单选考试单选考试单选                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=359886" title="不打不骂教孩子45招"><img src="http://www.coay.com/upload_cover/s/1379552508.jpg" height="100" alt="不打不骂教孩子45招" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=359886">不打不骂教孩子45招</a></div>
                    <div class="author">bigger</div>
                    <div class="des">
                    	令人反思的幼儿教育！                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=359421" title="燕子"><img src="http://www.coay.com/upload_cover/s/1378382644.jpg" height="100" alt="燕子" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=359421">燕子</a></div>
                    <div class="author">朱少麟 </div>
                    <div class="des">
                    	……当一束亮银色灯光投射在黑衣的她的身上，她所扮演的燕子翩翩舞起时，当场我落泪如雨，我的左冲右撞的灵魂终于凿开了决口，那只燕子从此栖进我心深处……在我眼中她简直是个传奇……一个脾气暴烈如同魔王的舞蹈教授，一个被排拒在舞台之外的天才舞者，一个总是在逃亡中的彷徨女子，交会在悲欢莫名的孤寂城市，互相曝露了深深的缺憾，又在泪光中见到了另一个用了解和希望照亮的世界，他们的心里都有一双翅膀，有时比肩，有时单飞，但飞行从没停歇，只为了追寻自尊与美……                    </div>
                </div>
                <div style="clear:both"></div>
            </div>

        <div style="padding:10px; text-align:center;"><font color="red">1</font> <a href="/catalog.php?p=2&amp;id=33">2</a> <a href="/catalog.php?p=3&amp;id=33">3</a> <a href="/catalog.php?p=4&amp;id=33">4</a> <a href="/catalog.php?p=5&amp;id=33">5</a> <a href="/catalog.php?p=6&amp;id=33">6</a> <a href="/catalog.php?p=7&amp;id=33">7</a> <a href="/catalog.php?p=8&amp;id=33">8</a> <a href="/catalog.php?p=9&amp;id=33">9</a> <a href=/catalog.php?p=2&amp;id=33 title="下一页">下一页</a> <a href=/catalog.php?p=11&amp;id=33 title="下十页">后十页</a> <a href=/catalog.php?p=60&amp;id=33 title="最后页">最后页</a> </div>

      </div>

      <div id="right">

      	<div>

            <div>
        <script type="text/javascript"> var cpro_id = 'u267363';</script>
<script type="text/javascript" src="http://cpro.baidu.com/cpro/ui/c.js"></script>        </div>

      		<div class="t" style="margin-top:10px;">分类</div>
           <ul style="padding:5px; margin:5px 5px 5px 15px;">
                            <li style="width:90px; float:left"><a href="catalog.php?id=31">婚恋·两性</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=32">青春·校园</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=33">亲子·教育</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=34">心理·励志</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=35">美容·养生</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=36">职场·理财</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=37">官场·商战</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=38">影视·时尚</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=39">漫画·绘本</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=40">历史·传记</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=41">思想·文化</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=42">社科·经典</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=43">文学·名著</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=44">军事·科幻</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=45">恐怖·悬疑</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=46">旅游·休闲</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=47">学习·资料</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=48">玄幻·奇幻</a></li>
                                <li style="width:90px; float:left"><a href="catalog.php?id=49">武侠·仙侠</a></li>
                            	<div style="clear:both"></div>
            </ul>
        </div>

                <h2 style="border-bottom:1px solid #006600; padding-bottom:5px;">本类推荐</h2>
                    <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=326437" title="孩子，把你的手给我"><img src="http://www.coay.com/upload_cover/s/1347162464.jpg" alt="孩子，把你的手给我" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=326437" title="孩子，把你的手给我">孩子，把你的手给我</a></div>
                    <div class="author">海姆·G·吉诺特</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=145538" title="捕捉儿童敏感期"><img src="http://www.coay.com/upload_cover/s/1313662967.jpg" alt="捕捉儿童敏感期" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=145538" title="捕捉儿童敏感期">捕捉儿童敏感期</a></div>
                    <div class="author">孙瑞雪</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=133844" title="风雨考研路"><img src="http://www.coay.com/upload_cover/s/1310301314.jpg" alt="风雨考研路" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=133844" title="风雨考研路">风雨考研路</a></div>
                    <div class="author">桑磊</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=130761" title="好妈妈胜过好老师"><img src="http://www.coay.com/upload_cover/s/1345804282.jpg" alt="好妈妈胜过好老师" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=130761" title="好妈妈胜过好老师">好妈妈胜过好老师</a></div>
                    <div class="author">尹建莉</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=104112" title="谁拿走了孩子的幸福"><img src="http://www.coay.com/upload_cover/s/1345804283.jpg" alt="谁拿走了孩子的幸福" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=104112" title="谁拿走了孩子的幸福">谁拿走了孩子的幸福</a></div>
                    <div class="author">李跃儿</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=98954" title="成功一定有方法"><img src="http://www.coay.com/upload_cover/s/1345804293.jpg" alt="成功一定有方法" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=98954" title="成功一定有方法">成功一定有方法</a></div>
                    <div class="author"></div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=96460" title="我在美国做妈妈"><img src="http://www.coay.com/upload_cover/s/1345804278.jpg" alt="我在美国做妈妈" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=96460" title="我在美国做妈妈">我在美国做妈妈</a></div>
                    <div class="author">蔡美儿</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=92597" title="好妈妈胜过好老师"><img src="http://www.coay.com/upload_cover/s/1345804275.jpg" alt="好妈妈胜过好老师" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=92597" title="好妈妈胜过好老师">好妈妈胜过好老师</a></div>
                    <div class="author">尹建莉</div>
                </div>
                <div style="clear:both"></div>
            </div>



        <div>
        <h2 style="border-bottom:1px solid #006600; padding-bottom:5px;">更多推荐</h2>
      		                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=337357"><img src="./upload_cover/s/1353574044.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=337357">大而不倒</a></div>
                </div>
                                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=247234"><img src="./upload_cover/s/1330607292.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=247234">货币战争4</a></div>
                </div>
                                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=337355"><img src="./upload_cover/s/1353573605.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=337355">《怪诞行为学2 非理性的积极力量》</a></div>
                </div>
                                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=335052"><img src="./upload_cover/s/1351764871.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=335052">青年创业课：三年之内成为富翁的人脉经营</a></div>
                </div>
                                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=334396"><img src="./upload_cover/s/1351340367.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=334396">好员工为什么会离你</a></div>
                </div>
                                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=334423"><img src="./upload_cover/s/1351355549.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=334423">大败局Ⅱ</a></div>
                </div>
                                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=93758"><img src="./upload_cover/s/1297528753.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=93758">丰乳肥臀</a></div>
                </div>
                                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=332230"><img src="./upload_cover/s/1349967930.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=332230">蛙</a></div>
                </div>
                                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=280097"><img src="./upload_cover/s/1337560958.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=280097">因为痛，所以叫青春</a></div>
                </div>
                                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=320050"><img src="./upload_cover/s/1344945652.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=320050">目送</a></div>
                </div>
                                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=329812"><img src="./upload_cover/s/1348836228.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=329812">白鹿原</a></div>
                </div>
                                <div class="book">
                	<div class="b_img"><a href="u_book.php?id=259621"><img src="./upload_cover/s/1333059011.jpg" height="100" /></a></div>
                    <div><a href="u_book.php?id=259621">《你若安好便是晴天》</a></div>
                </div>
                            <div style="clear:both"><a href="catalog2.php?id=33">更多</a></div>
        </div>
        </div>
      </div>

      <div class="cl"></div>
  </div>

	<div id="f_container">
      <div style="padding:10px;"><a href="http://www.coay.net" title="手游社区" target="_blank">手游社区</a></div>
       <div id="footer" style="text-align:right">&copy; 2012 epub电子书 all rights reserved</div>
       <div style="color:#999999; text-align:right; padding-bottom:10px 0">本站所有内容均由用户整理上传，如果发现有侵权作品，请及时跟我们联系，我们将第一时间作出处理。<br/>联系方式: <a href="mailto:coaybook@163.com">coaybook@163.com</a></div>
    </div>

    <div style="display:none"><script src="http://s11.cnzz.com/stat.php?id=2104515&web_id=2104515" language="JavaScript"></script></div>

<script type="text/javascript"> var cpro_id = 'u417038';</script><script src="http://cpro.baidu.com/cpro/ui/f.js" type="text/javascript"></script>
</body>
</html>

'''

max_page_re = re.compile(r'后十页</a>.+?p=(.+?)&amp;.+?title="最后页">', re.DOTALL)
page_nums = max_page_re.findall(s)
print page_nums