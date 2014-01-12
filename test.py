# -*- coding:UTF-8 -*-
import re

s = '''

﻿﻿<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link href="./css/style.css" rel="stylesheet" type="text/css" />
    <title>婚恋·两性 - epub电子书</title>
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
      	<h2 style="border-bottom:1px solid #006600; padding-bottom:5px;">婚恋·两性</h2>
                    <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367632" title="爱情"><img src="http://www.coay.com/upload_cover/s/1389557454.jpg" height="100" alt="爱情" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367632">爱情</a></div>
                    <div class="author">黄细海</div>
                    <div class="des">
                    	辅导班回复规划 规范化                     </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367622" title="天价皇后"><img src="http://www.coay.com/upload_cover/s/1389551308.jpg" height="100" alt="天价皇后" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367622">天价皇后</a></div>
                    <div class="author">吴笑笑</div>
                    <div class="des">
                    	天现异相，凤落相府，得凤者一统七国，有谁知？凤竟是那个名满天下的花痴女人。 丞相府的三小姐，花痴女人沐青瑶被南安王慕容流昭一拳打死了，却迎来了另一个全新的女人，光芒四射，魅力惊人。皇上，被休了！ 沐青瑶物语，即便你贵为皇帝，下了天价的骋礼，但我堂堂陆战军第17团的参谋长，竟然和别的女人共侍一夫，这样的男人，休！
                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367599" title="忘了要爱你"><img src="http://www.coay.com/upload_cover/s/1389531398.jpg" height="100" alt="忘了要爱你" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367599">忘了要爱你</a></div>
                    <div class="author">忘了要爱你</div>
                    <div class="des">
                    	忘了要爱你                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367598" title="爱是摧城拔寨"><img src="http://www.coay.com/upload_cover/s/1389531249.jpg" height="100" alt="爱是摧城拔寨" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367598">爱是摧城拔寨</a></div>
                    <div class="author">爱是摧城拔寨</div>
                    <div class="des">
                    	爱是摧城拔寨                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367597" title="爱是缠绵到死"><img src="http://www.coay.com/upload_cover/s/1389531217.jpg" height="100" alt="爱是缠绵到死" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367597">爱是缠绵到死</a></div>
                    <div class="author"></div>
                    <div class="des">
                    	爱是缠绵到死                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367595" title="石来运转"><img src="http://www.coay.com/upload_cover/s/1389529760.jpg" height="100" alt="石来运转" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367595">石来运转</a></div>
                    <div class="author">风吹翦羽</div>
                    <div class="des">
                    	风吹翦羽                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367594" title="侬本多情"><img src="http://www.coay.com/upload_cover/s/1389529317.jpg" height="100" alt="侬本多情" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367594">侬本多情</a></div>
                    <div class="author">浮图</div>
                    <div class="des">
                    	浮图                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367576" title="电子银行"><img src="http://www.coay.com/upload_cover/s/1389478180.jpg" height="100" alt="电子银行" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367576">电子银行</a></div>
                    <div class="author">丁芳</div>
                    <div class="des">
                    	打点滴                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367575" title="考试1"><img src="http://www.coay.com/upload_cover/s/1389478059.jpg" height="100" alt="考试1" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367575">考试1</a></div>
                    <div class="author">丁芳</div>
                    <div class="des">
                    	XXXX                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367556" title="天天被读者扎小人的坑神你伤不起！"><img src="http://www.coay.com/upload_cover/s/1389459638.jpg" height="100" alt="天天被读者扎小人的坑神你伤不起！" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367556">天天被读者扎小人的坑神你伤不起！</a></div>
                    <div class="author">时镜</div>
                    <div class="des">
                    	时镜                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367555" title="[金粉世家]重生秀珠"><img src="http://www.coay.com/upload_cover/s/1389459467.jpg" height="100" alt="[金粉世家]重生秀珠" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367555">[金粉世家]重生秀珠</a></div>
                    <div class="author">时镜</div>
                    <div class="des">
                    	时镜                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367554" title="凯撒革命"><img src="http://www.coay.com/upload_cover/s/1389459290.jpg" height="100" alt="凯撒革命" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367554">凯撒革命</a></div>
                    <div class="author">西子绪</div>
                    <div class="des">
                    	西子绪                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367553" title="总裁的7日恋人"><img src="http://www.coay.com/upload_cover/s/1389458227.jpg" height="100" alt="总裁的7日恋人" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367553">总裁的7日恋人</a></div>
                    <div class="author">安知晓</div>
                    <div class="des">
                    	“当我的女人。”第二次见面，他逼她当情人。他是冷漠无情的总裁，她是寄人篱下的伪千金。一次阴差阳错，他折磨她一天一夜，她略施小计报复，让他声名扫地，结下梁子。从此，她成为他的专属玩偶。为了家族生意，初恋情人，她假意留在他身边，虚情假意，最终假戏真做。然而，为了他的女人，一次游艇豪赌，他输掉了她。原来，活生生的人比不上死人一根头发。几年后，她成为享誉国际的珠宝设计师，依然逃不过他的魔爪，然而，心死的人，该如何再爱一次。ps：我笔下最悲催的女儿遇上一个最变态的男主，生了一个最强悍的闺女，又遇到史上最温柔男二的故                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367552" title="前妻，无你不寻欢"><img src="http://www.coay.com/upload_cover/s/1389458072.jpg" height="100" alt="前妻，无你不寻欢" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367552">前妻，无你不寻欢</a></div>
                    <div class="author"> 妖千千  </div>
                    <div class="des">
                    	浮华盛世之中，谁还会信仰爱情？入骨的缠绵，绯的是情，还是色？
*
她是众人眼中智商低下的傻子，
代替二小姐嫁给身份卑微的保镖之子，再门当户对不过了！
收敛起横溢才华，只为自己跟妈妈能够平安的生活下去。
本以为他会不愿娶个她这个傻子为妻……
“傻归傻……陪男人睡觉，总会吧？”男人的声音淡淡的，若有若无；却傲慢如帝王一般！
苏晓晨无语凝咽。她万万没想到：这个冷若冰霜的男人，竟然会对她这个傻子感“性”趣！！！
*
小三的一句：“我怀了你丈夫的孩子”，便将她活生生的打进了地狱；
自己委曲求全得                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367551" title=" 聂门：心期如画"><img src="http://www.coay.com/upload_cover/s/1389457475.jpg" height="100" alt=" 聂门：心期如画" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367551"> 聂门：心期如画</a></div>
                    <div class="author">殷寻</div>
                    <div class="des">
                    	冷桑清怎么也想不到，她会像打包行李一样被扔上飞机，并与聂门的人扯上关系。
聂门，她未曾听闻却在名流上层有着举足轻重的神秘家族。
每每面对他，或沉静或邪魅，多变的性格总令她深感困惑，却终于在见到两张一模一样的英俊面孔时恍然大悟。
那么，与她面对面优雅用餐的是谁？拥她入眠的——又是谁？
悲催的是，在如此混乱的情况下她的心房却开了花。
惊天秘密如同剥笋般层层揭开，却发现性情难测的他原来是最不能爱上的男人。
她惊恐迷离，是她无意打开了潘多拉盒子还是——卷入了一场早精心策划好的豪门商战？                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367500" title="豪门禁宠枕上欢"><img src="http://www.coay.com/upload_cover/s/1389380694.jpg" height="100" alt="豪门禁宠枕上欢" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367500">豪门禁宠枕上欢</a></div>
                    <div class="author">月下销魂</div>
                    <div class="des">
                    	他冷酷无情，习惯掌控一切，女人对他来说只是发泄生理需求的工具。一场交易，他囚禁了她，折磨着她，在她的身上发泄着最原始的需求。事后她退避三舍，他却步步紧逼，夜夜纠缠不休，但只有身体的欢愉，没有爱的承诺……
                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367497" title="都市寻欢"><img src="http://www.coay.com/upload_cover/s/1389377078.jpg" height="100" alt="都市寻欢" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367497">都市寻欢</a></div>
                    <div class="author">寻欢</div>
                    <div class="des">
                    	都市                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367495" title="和嫂子同居的日子"><img src="http://www.coay.com/upload_cover/s/1389374804.jpg" height="100" alt="和嫂子同居的日子" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367495">和嫂子同居的日子</a></div>
                    <div class="author">海龙号</div>
                    <div class="des">
                    	和嫂子同居的日子。。。。。。                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367493" title="我捡了一个少妇的手机"><img src="http://www.coay.com/upload_cover/s/1389360791.jpg" height="100" alt="我捡了一个少妇的手机" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367493">我捡了一个少妇的手机</a></div>
                    <div class="author">赵赶驴</div>
                    <div class="des">
                    	赵赶驴作品                    </div>
                </div>
                <div style="clear:both"></div>
            </div>
                        <div class="c_box">
            	<div class="l_b"><a href="u_book.php?id=367491" title="妒妃"><img src="http://www.coay.com/upload_cover/s/1389356664.jpg" height="100" alt="妒妃" /></a></div>
                <div class="r_b">
                	<div><a href="u_book.php?id=367491">妒妃</a></div>
                    <div class="author">MAX优</div>
                    <div class="des">
                    	**                    </div>
                </div>
                <div style="clear:both"></div>
            </div>

        <div style="padding:10px; text-align:center;"><font color="red">1</font> <a href="/catalog.php?p=2&amp;id=31">2</a> <a href="/catalog.php?p=3&amp;id=31">3</a> <a href="/catalog.php?p=4&amp;id=31">4</a> <a href="/catalog.php?p=5&amp;id=31">5</a> <a href="/catalog.php?p=6&amp;id=31">6</a> <a href="/catalog.php?p=7&amp;id=31">7</a> <a href="/catalog.php?p=8&amp;id=31">8</a> <a href="/catalog.php?p=9&amp;id=31">9</a> <a href=/catalog.php?p=2&amp;id=31 title="下一页">下一页</a> <a href=/catalog.php?p=11&amp;id=31 title="下十页">后十页</a> <a href=/catalog.php?p=1447&amp;id=31 title="最后页">最后页</a> </div>

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
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=273596" title="后宫如懿传"><img src="http://www.coay.com/upload_cover/s/1336765976.jpg" alt="后宫如懿传" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=273596" title="后宫如懿传">后宫如懿传</a></div>
                    <div class="author">流潋紫</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=267491" title="婚内婚外"><img src="http://www.coay.com/upload_cover/s/1335185960.jpg" alt="婚内婚外" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=267491" title="婚内婚外">婚内婚外</a></div>
                    <div class="author"></div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=184185" title="失恋33天"><img src="http://www.coay.com/upload_cover/s/1321748255.jpg" alt="失恋33天" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=184185" title="失恋33天">失恋33天</a></div>
                    <div class="author">鲍鲸鲸</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=171430" title="男人帮"><img src="http://www.coay.com/upload_cover/s/1319583711.jpg" alt="男人帮" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=171430" title="男人帮">男人帮</a></div>
                    <div class="author">唐浚</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=134658" title="裸婚"><img src="http://www.coay.com/upload_cover/s/1345096092.jpg" alt="裸婚" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=134658" title="裸婚">裸婚</a></div>
                    <div class="author">小唐</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=125516" title="云起(出版名:诱郎)"><img src="http://www.coay.com/upload_cover/s/1306799156.jpg" alt="云起(出版名:诱郎)" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=125516" title="云起(出版名:诱郎)">云起(出版名:诱郎)</a></div>
                    <div class="author">明月珰</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=121058" title="失恋33天"><img src="http://www.coay.com/upload_cover/s/1304686752.jpg" alt="失恋33天" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=121058" title="失恋33天">失恋33天</a></div>
                    <div class="author"> 鲍鲸鲸</div>
                </div>
                <div style="clear:both"></div>
            </div>

                        <div class="c_box" style="margin-top:5px">
            	<div class="l_b" style="width:80px; text-align:center"><a href="u_book.php?id=116599" title="幸福的苹果控"><img src="http://www.coay.com/upload_cover/s/1345096102.jpg" alt="幸福的苹果控" height="60" /></a></div>
                <div style="width:200px; float:right">
                	<div><a href="u_book.php?id=116599" title="幸福的苹果控">幸福的苹果控</a></div>
                    <div class="author">老草吃嫩牛</div>
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
                            <div style="clear:both"><a href="catalog2.php?id=31">更多</a></div>
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

bookDetail_re = re.compile(r"<h1>(.+?)</h1>.+?作者：(.+?)</p>.+?字数：(.+?)</p>.+?下载电子书.+?location='(.+?)'",
                               re.DOTALL)
x = bookDetail_re.findall(s)
print len(x)
print x
