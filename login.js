
		document.domain = 'yanxiu.com';
        //请求数据
        common.iframeAjax({
            domain:'i.yanxiu.com',
            method:'POST',
            url : "http://i.yanxiu.com/reg/getPlotformCount.tc",
            success:function(datas){
                dataObj = common.parseJson(datas);
                $('#bannerList .list1 .info').find('p').html('<em>'+ dataObj.resCount +'</em>&nbsp;&nbsp;教学/教研/科研/培训');
                $('#bannerList .list2 .info').find('p').html('<em>'+ dataObj.memberCount +'</em>&nbsp;&nbsp;校长/班主任/学科/幼教');
                $('#bannerList .list3 .info').find('p').html('<em>'+ dataObj.trainCount +'</em>&nbsp;&nbsp;国家级/地方级');
                $('#bannerList .list4 .info').find('p').html('<em>'+ dataObj.actCount +'</em>&nbsp;&nbsp;观课磨课/视频案例/解疑释难/专题讨论');
             },
            failure:function(){
                return false;
            }
        });
        common.doNotNeedRY = true;
        var url = 'http://i.yanxiu.com?j=true&fl=true';
        common.regist(function () {
            var backUrl = common.query("backUrl");
            var passport = require("common:widget/passport/passport");
            var $passport = $("#user");
            var $password = $("#pass");
            var $keepCookie = $("#pc");
            var $submit = $("#submit");
            var loginSuccess = function(){
                window.location.href = backUrl || "http://i.yanxiu.com?j=true&fl=true";
            }
            var check = function(info){
                if(!info.passport) {
                    return "账号不能为空";
                } else if(!info.password){
                    return "密码不能为空";
                }
                return null;
            };
            passport.init({
                appKey: "f6de93f8-c589-4aa7-9eb1-92f4afb4aea5"
            });

            if(passport.isLogin()) {
                // login from cookie
                var passport_val = passport.getPassport();
                var password_val = $password.val();
                var userid_val = passport.getUserId();
                var appid_val = passport.appid || 1234;
                var checkUserExist = function(){
                    $.ajax({
                        url:'http://pp.yanxiu.com/sso/makeUserExist.jsp',
                        type:'get',
                        dataType:'jsonp',
                        data:{
                            "username":passport_val,
                            "password":password_val,
                            "userid":userid_val,
                            "appid":appid_val
                        },
                        success:function(msg){
                            //alert(msg+"--cookie --success--"+JSON.stringify(msg));
                            var jsonRes = JSON.parse(JSON.stringify(msg));
                            //alert("json"+jsonRes.status);
                            if(jsonRes.status == true) {
                                loginSuccess();
                            }
                            return true;
                        },
                        error:function(msg) {
                            //alert(msg+"--cookie--failed--"+JSON.stringify(msg));
                            return false;
                        }
                    })
                };
                if(checkUserExist()) {
                    return true;
                }
            }

            passport.on("change:status", function(){
                fn.alert(passport.get("status"));
            });

            $submit.click(function(e) {
                // login from site
                e.preventDefault();
                var data = {
                    passport: $.trim($passport.val()),
                    password: $.trim($password.val()),
                    keepCookie: $keepCookie.prop("checked")
                };
                var err = check(data);
                if (err) {
                    fn.alert(err);
                    return;
                }

                var userid = $.trim($passport.val());
                var appid = passport.appid || 1234;
                var password = $.trim($password.val());
                var password = hex_md5($.trim($password.val()));
                var username = $.trim($passport.val());
                var s = (new Date()).getTime();
                var v = passport.version || 1;
                var persistentcookie = $keepCookie.prop("checked");
                $.ajax({
                    url: 'http://pp.yanxiu.com/sso/loginNew.jsp',
                    type: 'get',
                    dataType: 'jsonp',
                    data: {
                        "userid": userid,   //userid here is username
                        "appid": appid,
                        "password": password,
                        "username": username,
                        "s": s,
                        "v": v,
                        "persistentcookie": persistentcookie
                    },
                    success: function (msg) {
                        // check user in ucenter database
                        //alert(msg + "--login--success--" + JSON.stringify(msg));
                        var jsonRes = JSON.parse(JSON.stringify(msg));
                        if(jsonRes.hasOwnProperty("login_status") && jsonRes.login_status != 0) {
                            if (jsonRes.login_status == 13) {
                                var url = "http://pp.yanxiu.com/web/remind_activate.jsp?problem=6";
                                if (passport.loginRedirectUrl != "") {
                                    url += "?backUrl=" + escape(passport.loginRedirectUrl) + '&problem=7'
                                }
                                window.location = url
                            } else if (jsonRes.login_status == 2) {
                                fn.alert('用户名或密码错误');
                                _hmt.push(['_trackEvent', '登录失败事件数-用户名或密码', '按钮', '点击量']);//百度统计，失败
                                passport.passwdInput.focus();
                            } else if (jsonRes.login_status == 14) {
                                var url = "http://pp.yanxiu.com/reg/toAddMessage.tc?passport=" + jsonRes.tmpPassport + '&problem=8';
                                if (this.loginRedirectUrl != "") {
                                    url += "&backUrl=" + escape(passport.loginRedirectUrl)
                                }
                                window.location = url
                            } else if (jsonRes.login_status == 11) {
                                fn.alert('服务器故障，请稍候再试');
                                _hmt.push(['_trackEvent', '登录失败事件数-服务器故障', '按钮', '点击量']);//百度统计，失败
                                passport.passwdInput.focus();
                            } else if (jsonRes.login_status == 15) {
                                fn.alert('用户已被合并注销');
                                _hmt.push(['_trackEvent', '登录失败事件数-用户已注销', '按钮', '点击量']);//百度统计，失败
                                passport.passwdInput.focus();
                            } else {
                                fn.alert('登录失败，请稍后重试');
                                _hmt.push(['_trackEvent', '登录失败事件数', '按钮', '点击量']);//百度统计，失败
                                passport.passwdInput.focus();
                            }
                            return false;
                        }
                        if(jsonRes.hasOwnProperty("passport")) {
                            data.passport = jsonRes.passport;
                        }
                        passport.login(data).then(function (err) {
                            if (err) {
                                fn.alert(err.msg);
                            } else {
                                loginSuccess();
                            }
                        });
                        _hmt.push(['_trackEvent', '成功登陆事件数', '按钮', '点击量']);//百度统计，成功
                        return true;
                    },
                    error: function (msg) {
                        //alert(msg + "--login--failed--" + JSON.stringify(msg));
                        fn.alert('登录失败，请稍后重试');
                        return false;
                    }
                });
            });
        });
    