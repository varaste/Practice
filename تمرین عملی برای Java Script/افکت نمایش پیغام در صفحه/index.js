<head> 
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js"></script>
<style>
.message-box {
padding: 15px;
text-align: center;
border-radius: 5px;
background-color: #e5e5e5;
display: none;
box-shadow: 0 0 4px 0 #666;
border: 1px solid #fff;
font: normal 13px tahoma;
position: fixed;
width: 40%;
top: 25px;
left: 30%;
z-index: 50;
text-shadow: 0 0 1px #fff;
direction: rtl;
}
.message-box img {
vertical-align: middle;
}
.screen {
position: fixed;
width: 100%;
height: 100%;
opacity: .7;
background-color: #fff;
top:0;
left:0;
z-index:45;
display:none;
padding:0;
margin:0;
}
.sample-btn {
font: normal 12px tahoma;
padding: 5px 10px;
}
</style>
<script>
function showMessage(){
$('.message-box').slideDown().delay(3000).slideUp();
$('.screen').delay(3500).fadeOut();
}

$(function(){
$('.sample-btn').on('click',function(){$('.screen').fadeIn(),showMessage()});

});
</script>
</head>
<body>

<div class="message-box"><img src="images/tick-32px.png" alt="" /> محل نمایش پیغام مورد نظر شما</div>
<button class="sample-btn">نمایش پیغام</button> 
<div class="screen"></div>
</body>