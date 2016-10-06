// jQuery Transit © 2011-2014+, Rico Sta. Cruz. Released under the MIT License.
(function(t,e){if(typeof define==="function"&&define.amd){define(["jquery"],e)}else if(typeof exports==="object"){module.exports=e(require("jquery"))}else{e(t.jQuery)}})(this,function(t){t.transit={version:"0.9.12",propertyMap:{marginLeft:"margin",marginRight:"margin",marginBottom:"margin",marginTop:"margin",paddingLeft:"padding",paddingRight:"padding",paddingBottom:"padding",paddingTop:"padding"},enabled:true,useTransitionEnd:false};var e=document.createElement("div");var n={};function i(t){if(t in e.style)return t;var n=["Moz","Webkit","O","ms"];var i=t.charAt(0).toUpperCase()+t.substr(1);for(var r=0;r<n.length;++r){var s=n[r]+i;if(s in e.style){return s}}}function r(){e.style[n.transform]="";e.style[n.transform]="rotateY(90deg)";return e.style[n.transform]!==""}var s=navigator.userAgent.toLowerCase().indexOf("chrome")>-1;n.transition=i("transition");n.transitionDelay=i("transitionDelay");n.transform=i("transform");n.transformOrigin=i("transformOrigin");n.filter=i("Filter");n.transform3d=r();var a={transition:"transitionend",MozTransition:"transitionend",OTransition:"oTransitionEnd",WebkitTransition:"webkitTransitionEnd",msTransition:"MSTransitionEnd"};var o=n.transitionEnd=a[n.transition]||null;for(var u in n){if(n.hasOwnProperty(u)&&typeof t.support[u]==="undefined"){t.support[u]=n[u]}}e=null;t.cssEase={_default:"ease","in":"ease-in",out:"ease-out","in-out":"ease-in-out",snap:"cubic-bezier(0,1,.5,1)",easeInCubic:"cubic-bezier(.550,.055,.675,.190)",easeOutCubic:"cubic-bezier(.215,.61,.355,1)",easeInOutCubic:"cubic-bezier(.645,.045,.355,1)",easeInCirc:"cubic-bezier(.6,.04,.98,.335)",easeOutCirc:"cubic-bezier(.075,.82,.165,1)",easeInOutCirc:"cubic-bezier(.785,.135,.15,.86)",easeInExpo:"cubic-bezier(.95,.05,.795,.035)",easeOutExpo:"cubic-bezier(.19,1,.22,1)",easeInOutExpo:"cubic-bezier(1,0,0,1)",easeInQuad:"cubic-bezier(.55,.085,.68,.53)",easeOutQuad:"cubic-bezier(.25,.46,.45,.94)",easeInOutQuad:"cubic-bezier(.455,.03,.515,.955)",easeInQuart:"cubic-bezier(.895,.03,.685,.22)",easeOutQuart:"cubic-bezier(.165,.84,.44,1)",easeInOutQuart:"cubic-bezier(.77,0,.175,1)",easeInQuint:"cubic-bezier(.755,.05,.855,.06)",easeOutQuint:"cubic-bezier(.23,1,.32,1)",easeInOutQuint:"cubic-bezier(.86,0,.07,1)",easeInSine:"cubic-bezier(.47,0,.745,.715)",easeOutSine:"cubic-bezier(.39,.575,.565,1)",easeInOutSine:"cubic-bezier(.445,.05,.55,.95)",easeInBack:"cubic-bezier(.6,-.28,.735,.045)",easeOutBack:"cubic-bezier(.175, .885,.32,1.275)",easeInOutBack:"cubic-bezier(.68,-.55,.265,1.55)"};t.cssHooks["transit:transform"]={get:function(e){return t(e).data("transform")||new f},set:function(e,i){var r=i;if(!(r instanceof f)){r=new f(r)}if(n.transform==="WebkitTransform"&&!s){e.style[n.transform]=r.toString(true)}else{e.style[n.transform]=r.toString()}t(e).data("transform",r)}};t.cssHooks.transform={set:t.cssHooks["transit:transform"].set};t.cssHooks.filter={get:function(t){return t.style[n.filter]},set:function(t,e){t.style[n.filter]=e}};if(t.fn.jquery<"1.8"){t.cssHooks.transformOrigin={get:function(t){return t.style[n.transformOrigin]},set:function(t,e){t.style[n.transformOrigin]=e}};t.cssHooks.transition={get:function(t){return t.style[n.transition]},set:function(t,e){t.style[n.transition]=e}}}p("scale");p("scaleX");p("scaleY");p("translate");p("rotate");p("rotateX");p("rotateY");p("rotate3d");p("perspective");p("skewX");p("skewY");p("x",true);p("y",true);function f(t){if(typeof t==="string"){this.parse(t)}return this}f.prototype={setFromString:function(t,e){var n=typeof e==="string"?e.split(","):e.constructor===Array?e:[e];n.unshift(t);f.prototype.set.apply(this,n)},set:function(t){var e=Array.prototype.slice.apply(arguments,[1]);if(this.setter[t]){this.setter[t].apply(this,e)}else{this[t]=e.join(",")}},get:function(t){if(this.getter[t]){return this.getter[t].apply(this)}else{return this[t]||0}},setter:{rotate:function(t){this.rotate=b(t,"deg")},rotateX:function(t){this.rotateX=b(t,"deg")},rotateY:function(t){this.rotateY=b(t,"deg")},scale:function(t,e){if(e===undefined){e=t}this.scale=t+","+e},skewX:function(t){this.skewX=b(t,"deg")},skewY:function(t){this.skewY=b(t,"deg")},perspective:function(t){this.perspective=b(t,"px")},x:function(t){this.set("translate",t,null)},y:function(t){this.set("translate",null,t)},translate:function(t,e){if(this._translateX===undefined){this._translateX=0}if(this._translateY===undefined){this._translateY=0}if(t!==null&&t!==undefined){this._translateX=b(t,"px")}if(e!==null&&e!==undefined){this._translateY=b(e,"px")}this.translate=this._translateX+","+this._translateY}},getter:{x:function(){return this._translateX||0},y:function(){return this._translateY||0},scale:function(){var t=(this.scale||"1,1").split(",");if(t[0]){t[0]=parseFloat(t[0])}if(t[1]){t[1]=parseFloat(t[1])}return t[0]===t[1]?t[0]:t},rotate3d:function(){var t=(this.rotate3d||"0,0,0,0deg").split(",");for(var e=0;e<=3;++e){if(t[e]){t[e]=parseFloat(t[e])}}if(t[3]){t[3]=b(t[3],"deg")}return t}},parse:function(t){var e=this;t.replace(/([a-zA-Z0-9]+)\((.*?)\)/g,function(t,n,i){e.setFromString(n,i)})},toString:function(t){var e=[];for(var i in this){if(this.hasOwnProperty(i)){if(!n.transform3d&&(i==="rotateX"||i==="rotateY"||i==="perspective"||i==="transformOrigin")){continue}if(i[0]!=="_"){if(t&&i==="scale"){e.push(i+"3d("+this[i]+",1)")}else if(t&&i==="translate"){e.push(i+"3d("+this[i]+",0)")}else{e.push(i+"("+this[i]+")")}}}}return e.join(" ")}};function c(t,e,n){if(e===true){t.queue(n)}else if(e){t.queue(e,n)}else{t.each(function(){n.call(this)})}}function l(e){var i=[];t.each(e,function(e){e=t.camelCase(e);e=t.transit.propertyMap[e]||t.cssProps[e]||e;e=h(e);if(n[e])e=h(n[e]);if(t.inArray(e,i)===-1){i.push(e)}});return i}function d(e,n,i,r){var s=l(e);if(t.cssEase[i]){i=t.cssEase[i]}var a=""+y(n)+" "+i;if(parseInt(r,10)>0){a+=" "+y(r)}var o=[];t.each(s,function(t,e){o.push(e+" "+a)});return o.join(", ")}t.fn.transition=t.fn.transit=function(e,i,r,s){var a=this;var u=0;var f=true;var l=t.extend(true,{},e);if(typeof i==="function"){s=i;i=undefined}if(typeof i==="object"){r=i.easing;u=i.delay||0;f=typeof i.queue==="undefined"?true:i.queue;s=i.complete;i=i.duration}if(typeof r==="function"){s=r;r=undefined}if(typeof l.easing!=="undefined"){r=l.easing;delete l.easing}if(typeof l.duration!=="undefined"){i=l.duration;delete l.duration}if(typeof l.complete!=="undefined"){s=l.complete;delete l.complete}if(typeof l.queue!=="undefined"){f=l.queue;delete l.queue}if(typeof l.delay!=="undefined"){u=l.delay;delete l.delay}if(typeof i==="undefined"){i=t.fx.speeds._default}if(typeof r==="undefined"){r=t.cssEase._default}i=y(i);var p=d(l,i,r,u);var h=t.transit.enabled&&n.transition;var b=h?parseInt(i,10)+parseInt(u,10):0;if(b===0){var g=function(t){a.css(l);if(s){s.apply(a)}if(t){t()}};c(a,f,g);return a}var m={};var v=function(e){var i=false;var r=function(){if(i){a.unbind(o,r)}if(b>0){a.each(function(){this.style[n.transition]=m[this]||null})}if(typeof s==="function"){s.apply(a)}if(typeof e==="function"){e()}};if(b>0&&o&&t.transit.useTransitionEnd){i=true;a.bind(o,r)}else{window.setTimeout(r,b)}a.each(function(){if(b>0){this.style[n.transition]=p}t(this).css(l)})};var z=function(t){this.offsetWidth;v(t)};c(a,f,z);return this};function p(e,i){if(!i){t.cssNumber[e]=true}t.transit.propertyMap[e]=n.transform;t.cssHooks[e]={get:function(n){var i=t(n).css("transit:transform");return i.get(e)},set:function(n,i){var r=t(n).css("transit:transform");r.setFromString(e,i);t(n).css({"transit:transform":r})}}}function h(t){return t.replace(/([A-Z])/g,function(t){return"-"+t.toLowerCase()})}function b(t,e){if(typeof t==="string"&&!t.match(/^[\-0-9\.]+$/)){return t}else{return""+t+e}}function y(e){var n=e;if(typeof n==="string"&&!n.match(/^[\-0-9\.]+/)){n=t.fx.speeds[n]||t.fx.speeds._default}return b(n,"ms")}t.transit.getTransitionValue=d;return t});

var supports = (function() {
   var div = document.createElement('div'),
      vendors = 'Khtml Ms O Moz Webkit'.split(' '),
      len = vendors.length;
 
   return function(prop) {
      if ( prop in div.style ) return true;
 
      prop = prop.replace(/^[a-z]/, function(val) {
         return val.toUpperCase();
      });
 
      while(len--) {
         if ( vendors[len] + prop in div.style ) {
            return true;
         }
      }
      return false;
   };
})();

jQuery(function ($) {
	$(document).ready(function() {
        var image_max = 2;
        var current_index = 1;
        var checkIng = 0;
        var change_speed = 700;
        var change_delay = 6000;
        var move_val = 1024;
        var p_move_val;
        var left_dir = 1;
        var right_dir = 2;
        var support_css_check = 0;

        if (supports('transition')) { support_css_check = 1; }
        else { support_css_check = 0; }

        function get_next_index(newCurrentIndex,newDir,newTargetIndex) {
            var target_index;
            var prev_index;
            var next_index;
            var temp_index;

            if(newTargetIndex == '') {
                if(newDir == left_dir) {
                    target_index = parseInt(newCurrentIndex, 10) - 1;
                    if(target_index <= 0) {
                        target_index = image_max;
                    }
                }
                else {
                    target_index = parseInt(newCurrentIndex, 10) + 1;
                    if(target_index > image_max) {
                        target_index = 1;
                    }
                }
            }
            else {
                target_index = newTargetIndex;
            }

            prev_index = parseInt(target_index, 10) - 1;
            if(prev_index <= 0) {
                prev_index = image_max;
            }

            next_index = parseInt(target_index, 10) + 1;
            if(next_index > image_max) {
                next_index = 1;
            }

            temp_index = parseInt(next_index, 10) + 1;
            if(temp_index > image_max) {
                temp_index = 1;
            }

            return [prev_index,target_index,next_index,temp_index];
        }

        var auto_move = setTimeout(function() {
            move(right_dir,'');
        }, change_delay);

        function move(newDir, newIndex) {
            if(checkIng !== 0) { return; }
            checkIng = 1;

            clearInterval(auto_move);

            var index_ary = get_next_index(current_index,newDir,newIndex);

            var temp_index = index_ary[1];

            var t_left1 = move_val;
            var t_left2 = t_left1*-1;
            var temp_left = move_val;
            if(newDir == left_dir) {
                temp_index = index_ary[1];

                t_left1 = t_left2;
                t_left2 = t_left1*-1;
                temp_left = move_val*-1;
            }

            $('.spot_page a').each(function() {
                $(this).removeClass('aon');
            });
            $('#spot_page_'+index_ary[1]).addClass('aon');

            $('.spot_image2').css('left',temp_left+'px').css('display','block');
            $('.spot_image2 img').attr('src', '../static/images/main/main_visual_0'+temp_index+'.jpg');

            if (support_css_check == 1) {
                $('.slider').transition({x:'+='+t_left2},change_speed,function() {
                    end_move_transition(index_ary);
                });
            }
            else {
                $('.slider').animate({left:t_left2},change_speed,function() {
                    end_move(index_ary);
                });
            }
        }

        function end_move_transition(newIndexAry) {
            $('.spot_image img').attr('src', '../static/images/main/main_visual_0'+newIndexAry[1]+'.jpg')
            $('.slider').transition({x:'0'},0);
            $('.spot_image2').css('display','none').css('left','0px');

            current_index = newIndexAry[1];

            checkIng--;if(checkIng <= 0) {checkIng = 0;}

            auto_move = setTimeout(function() {
                move(right_dir,'');
            }, change_delay);
        }

        function end_move(newIndexAry) {
            $('.spot_image img').attr('src', '../static/images/main/main_visual_0'+newIndexAry[1]+'.jpg')
            $('.spot_image2').css('left','0px');
            $('.slider').css('left','0px');

            current_index = newIndexAry[1];

            checkIng--;if(checkIng <= 0) {checkIng = 0;}

            auto_move = setTimeout(function() {
                move(right_dir,'');
            }, change_delay);
        }

        $('.spot_page a').click(function() {
            var t_id = $(this).attr('id').substr(10);

            if(current_index == t_id) { return; }

            if(t_id > current_index) {
                move(right_dir,t_id);
            }
            else {
                move(left_dir,t_id);
            }
        });

        $('.btn_spot_left').click(function() {
            move(left_dir,'');
        });

        $('.btn_spot_rig').click(function() {
            move(right_dir,'');
        });

        var resizeEndCheker;
        var pmenu_li_moveval = 0;
        $(window).resize(function() {
            checkIng = 1;

            clearInterval(resizeEndCheker);
            resizeEndCheker = setTimeout(function() {
                checkIng = 0;

                clearInterval(auto_move);
                auto_move = setTimeout(function() {
                    move(right_dir,'');
                }, change_delay);
            }, 50);

            var window_width = $(window).width();
            if(window_width < 1024) {
                move_val = window_width;
            }
            else {
                move_val = 1024;
            }
            
            $('.lst_spot li').width(move_val);
            $('.slider').transition({x:'0'},0);
            $('.slider').css('left','0px');
            $('.spot_image2').css('left','0px');

            // pmenu
            if(window_width <= 518) {
                pmenu_li_moveval = $('.pmenu').width();
                $('.ins_pmenu li').width(pmenu_li_moveval);

                $('.ins_pmenu').width($('.ins_pmenu li').width()*4 + 8);
            }
            else if(window_width <= 759) {
                pmenu_li_moveval = $('.pmenu').width()/2 -2;
                $('.ins_pmenu li').width(pmenu_li_moveval);

                $('.ins_pmenu').width($('.ins_pmenu li').width()*4 + 8);
            }
            else {
                $('.ins_pmenu li').css('width','calc(25% - 2px)');

                $('.ins_pmenu').css('width', '100%');
            }
        });
        $(window).resize();

        $('.btn_pnb_left').click(function() {
            if(checkIng !== 0) { return; }
            checkIng = 1;

            if (support_css_check == 1) {
                p_move_val = (pmenu_li_moveval + 2);

                $('.ins_pmenu li').last().insertBefore($('.ins_pmenu li').eq(0));
                $('.ins_pmenu').css('x',p_move_val*-1+'px');

                $('.ins_pmenu').transition({x:'+='+p_move_val},change_speed,function() {
                    checkIng = 0;
                });
            }
            else {
                p_move_val = (pmenu_li_moveval + 2);

                $('.ins_pmenu li').last().insertAfter($('.ins_pmenu li').eq(0));
                $('.ins_pmenu').css('left',p_move_val*-1+'px');

                $('.slider').animate({left:p_move_val},change_speed,function() {
                    checkIng = 0;
                });
            }
        });
        $('.btn_pnb_rig').click(function() {
            if(checkIng !== 0) { return; }
            checkIng = 1;

            if (support_css_check == 1) {
                p_move_val = (pmenu_li_moveval + 2)*-1;
                $('.ins_pmenu').transition({x:'+='+p_move_val},change_speed,function() {
                    $('.ins_pmenu li').eq(0).insertAfter($('.ins_pmenu li').last());
                    $('.ins_pmenu').transition({x:'0'},0);
                    checkIng = 0;
                });
            }
            else {
                p_move_val = (pmenu_li_moveval + 2)*-1;
                $('.slider').animate({left:p_move_val},change_speed,function() {
                    $('.ins_pmenu li').eq(0).insertAfter($('.ins_pmenu li').last());
                    $('.ins_pmenu').css('left','0px');
                    checkIng = 0;
                });
            }
        });

        var banner_dir = -1;
        function move_loop() {
            var c_left = $('.lst_b1').css('left');
            var c_left_val = c_left.substr(0, c_left.length - 2) * banner_dir;
            var t_move_val = (parseInt(c_left_val) + 1)*banner_dir;
            
            if(t_move_val > 68) {
                if(banner_dir == 1) {
                    for(var i = 0; i < 28; i++) {
                        $('.lst_b1 li').last().insertAfter($('.lst_b1 li').eq(0));
                        $('.lst_b1 li').eq(0).insertAfter($('.lst_b1 li').eq(1));
                    }

                    $('.lst_b1').css('left','-5564px');
                }
                
                move_loop();
                return;
            }
            else if(t_move_val < -5564) {
                if(banner_dir == -1) {
                    for(var i = 0; i < 28; i++) {
                        $('.lst_b1 li').eq(0).insertAfter($('.lst_b1 li').last());
                    }

                    $('.lst_b1').css('left','67px');
                }

                move_loop();
                return;
            }

            $('.lst_b1').stop().clearQueue().animate({left:t_move_val+'px'}, 20, 'linear', move_loop);
        }
        move_loop();

        $('.lst_b1').hover(function(){
            $('.lst_b1').stop().clearQueue();
        }, function() {
            move_loop();
        });

        $('.btn_roll_left').click(function() {
            console.log('left');
            banner_dir = -1;
            move_loop();
        });

        $('.btn_roll_rig').click(function() {
            console.log('right');
            banner_dir = 1;
            move_loop();
        });

        $('.btn_menu_m').click(function() {
            $('#layer_bg').toggle();
            $('#mnb_m').toggle();  
        });
        $('#layer_bg').click(function() {
            $('#layer_bg').toggle();
            $('#mnb_m').toggle();  
        });
    });
});

// mnb
jQuery(function ($) {
    $('#mnb_p > li').hover(function() {
        $(this).children('.mnb_sub_menu').show();
    }, function() {
        $(this).children('.mnb_sub_menu').hide();
    });

    $('#mnb_m > li').click(function() {
        $(this).children('.mnb_sub_menu').toggle();
    });
});
