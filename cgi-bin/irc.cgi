<!-- This is part of CGI:IRC 0.5
  == http://cgiirc.sourceforge.net/
  == Copyright (C) 2000-2002 David Leadbeater <cgiirc@dgl.cx>
  == Released under the GNU GPL
  -->

<html>
<head>
<link rel="SHORTCUT ICON" href="/www/images/favicon.ico">
<script language="JavaScript"><!--
function setjs() {
 if(navigator.product == 'Gecko') {
   document.loginform["interface"].value = 'mozilla';
 }else if(window.opera && document.childNodes) {
   document.loginform["interface"].value = 'opera7';
 }else if(navigator.appName == 'Microsoft Internet Explorer' &&
    navigator.userAgent.indexOf("Mac_PowerPC") > 0) {
    document.loginform["interface"].value = 'konqueror';
 }else if(navigator.appName == 'Microsoft Internet Explorer' &&
 document.getElementById && document.getElementById('ietest').innerHTML) {
   document.loginform["interface"].value = 'ie';
 }else if(navigator.appName == 'Konqueror') {
    document.loginform["interface"].value = 'konqueror';
 }else if(window.opera) {
   document.loginform["interface"].value = 'opera';
 }
}
function nickvalid() {
   var nick = document.loginform.Nickname.value;
   if(nick.match(/^[A-Za-z0-9\[\]\{\}^\\\|\_\-`]{1,32}$/))
      return true;
   alert('Please enter a valid nickname');
   document.loginform.Nickname.value = nick.replace(/[^A-Za-z0-9\[\]\{\}^\\\|\_\-`]/g, '');
   return false;
}
//-->
</script>
<title>CGI:IRC Login</title>
</head>
<body bgcolor="#ffffff" text="#000000"><!-- begin banner code -->

<table bgcolor="#000000" align="center" border="0" cellpadding="1" cellspacing="0" width="728">
<tr>
<td width="100%">
    <table background="/nf-images/nf_back.gif" border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="#E7E7E7">
    <tr>
 
        <td width="10%">
        <a href="http://www.netfirms.com"><img alt="Free Web Hosting by Netfirms" align="absmiddle" border="0" src="/nf-images/Freewebhosting.gif" width="184" height="24"></a><br />
        </td>

        <td width="90%">

        <font size="2"><a href="http://www.netfirms.com">Web Hosting by <b>Netfirms</b></a> | <a href="http://www.netfirms.com/domain-names">Free Domain Names by <b>Netfirms</b></a></font>
        </td>

    </tr>
    </table>   
    
</td>
</tr>
</table>

<table align="center" border="0" cellpadding="1" cellspacing="0" width="728">
<tr>
<td width="100%">

<img src="/nf-images/freewebhosting.webhosting.asis" width="1" height="3"><br />

<!-- Start Creative for 728 x 90 format from Google -->
<script type="text/javascript" language="JavaScript">
<!--
         google_ad_client = 'netfirms_728x90';
         google_ad_width = 728;
         google_ad_height = 90;
         google_ad_format = '728x90_sln';
         google_safe = 'high';
// -->
</script>
<script type="text/javascript" language="JavaScript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script><br />
<noscript>
<img height=1 width=1 border=0 src="http://pagead2.googlesyndication.com/pagead/imp.gif?client=ca-netfirms_728x90&event=noscript"/><br /></noscript>
<!-- End Creative for 728 x 90 format from Google -->

</td>
</tr>
</table>

<!-- end banner code -->

<form method="post" action="irc.cgi" name="loginform" onsubmit="setjs();return nickvalid()">
<input type="hidden" name="interface" value="nonjs">
<table border="0" cellpadding="5" cellspacing="0">
<tr><td colspan="2" align="center" bgcolor="#c0c0dd"><b>CGI:IRC
Login</b></td></tr>
<tr><td align="right" bgcolor="#f1f1f1">Nickname</td><td align="left"
bgcolor="#f1f1f1"><input type="text" name="Nickname" value="JArcane"></td></tr>
<tr><td align="right" bgcolor="#f1f1f1">Server</td><td align="left"
bgcolor="#f1f1f1"><input type="text" name="Server" value="irc.magicstar.net" disabled="1"></td></tr>
<tr><td align="right" bgcolor="#f1f1f1">Channel</td><td align="left"
bgcolor="#f1f1f1"><input type="text" name="Channel" value="#rpgnet" disabled="1"></td></tr>
<tr><td align="left" bgcolor="#d9d9d9">
<small><a href="irc.cgi?adv=1">Advanced..</a></small>
</td><td align="right" bgcolor="#d9d9d9">
<input type="submit" value="Login" style="background-color: #d9d9d9">
</td></tr></table></form>

<small id="ietest"><a href="http://cgiirc.sourceforge.net/">CGI:IRC</a> 0.5.4 (2004/01/29)<br />
</small>
</body></html>
