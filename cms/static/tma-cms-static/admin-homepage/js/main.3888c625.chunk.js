(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{201:function(e,t,a){e.exports=a.p+"static/media/icon.831c46b9.png"},209:function(e,t,a){e.exports=a(431)},214:function(e,t,a){},431:function(e,t,a){"use strict";a.r(t);var n=a(68),l=a(69),s=a(71),i=a(70),o=a(31),c=a(72),u=a(0),r=a.n(u),d=a(16),m=a.n(d),g=(a(214),a(52)),b=a(89),p=a(203),h=a(478),E=a(468),y=a(470),f=a(199),_=a.n(f),C=a(200),T=a.n(C),k=a(471),N=a(483),B=a(481),v=a(472),I=a(473),O=a(482);var j=function(e){var t=r.a.useState(!1),a=Object(p.a)(t,2),n=a[0],l=a[1],s="tuileDoubleRebondOri",i="doubleRebondTulletIcon",o=e.keyId,c=function(){l(!1)};return e.keyId?(s="tuileDoubleRebond"+e.keyId,i="doubleRebondTulletIcon"+e.keyId):o="original",r.a.createElement("div",{className:"tuileDoubleRebond contentManage"},r.a.createElement("h2",null,e.title),r.a.createElement(E.a,null,r.a.createElement(y.a,null,r.a.createElement(h.a,{fullWidth:!0,className:s+" fieldTuileDoubleRebond",keyid:e.keyId,onChange:function(t){e.handleChangeInput(t,!1,"image")},onFocus:function(){document.getElementsByClassName(i)[0].style.backgroundColor="rgb(92, 183, 216)"},onBlur:function(e){document.getElementsByClassName(i)[0].style.backgroundColor=""},label:"Image",value:e.static_double?e.static_double.image:"",InputProps:{endAdornment:r.a.createElement(N.a,{position:"end"},r.a.createElement(k.a,{edge:"end","aria-label":"Toggle Image",onClick:function(){l(!0)}},r.a.createElement(_.a,{size:"small"})))}}),r.a.createElement(B.a,{"aria-labelledby":"simple-modal-title","aria-describedby":"simple-modal-description",open:n,onClose:c},r.a.createElement(v.a,{container:!0,spacing:0,direction:"row",alignItems:"center",justify:"center",style:{minHeight:"100vh",maxHeight:"100%",overflow:"auto"}},r.a.createElement(v.a,{className:"displayPreviewImage",item:!0,sm:9,xs:10},r.a.createElement("img",{src:e.static_double?e.static_double.image:"",alt:e.static_double?e.static_double.image:""}),r.a.createElement("div",{className:"closeButton"},r.a.createElement(I.a,{color:"secondary",onClick:c,size:"small",className:"fabWrapperCloseButton"},r.a.createElement(T.a,{className:"closeColor"})))))),r.a.createElement(h.a,{fullWidth:!0,className:s+" fieldTuileDoubleRebond",keyid:e.keyId,onChange:function(t){e.handleChangeInput(t,!1,"link")},onFocus:function(){document.getElementsByClassName(i)[0].style.backgroundColor="rgb(92, 183, 216)"},onBlur:function(e){document.getElementsByClassName(i)[0].style.backgroundColor=""},label:"Lien",onClick:c,value:e.static_double?e.static_double.link:"",InputProps:{endAdornment:r.a.createElement(N.a,{position:"end"},r.a.createElement(O.a,{checked:e.static_double?e.static_double.target_blank:"",onChange:function(){e.handleTargetBlank(o)},value:"target_blank",inputProps:{"aria-label":"primary checkbox"}}))}}))))},D=function(e){return r.a.createElement("div",{className:"tuileDouble contentManage"},r.a.createElement("h2",null,"Tuile double"),r.a.createElement(E.a,null,r.a.createElement(y.a,null,r.a.createElement(h.a,{className:"fieldTuileDouble",fullWidth:!0,onChange:function(t){e.handleChangeInput(t)},onFocus:function(){document.getElementsByClassName("doublesimpleTulletIcon")[0].style.backgroundColor="rgb(92, 183, 216)"},onBlur:function(e){document.getElementsByClassName("doublesimpleTulletIcon")[0].style.backgroundColor=""},label:"Course_id: 9",value:e.double?e.double:""}))))},S=function(e){return r.a.createElement("div",{className:"tuilesSimple contentManage"},r.a.createElement("h2",null,"Tuiles simples"),r.a.createElement(E.a,{className:"card"},r.a.createElement(y.a,{className:"inputLilTuile"},e.single.map(function(t,a){return r.a.createElement(h.a,{className:"fieldSingle",key:a,fullWidth:!0,onChange:function(t){e.handleChangeInput(t,a)},label:"Course_id: "+parseInt(a+1),onFocus:function(){document.getElementsByClassName("simpleTulletIcon")[a].style.backgroundColor="rgb(92, 183, 216)"},onBlur:function(e){document.getElementsByClassName("simpleTulletIcon")[a].style.backgroundColor=""},value:t})}))))},R=a(474),x=a(432),w=function(e){function t(){return Object(n.a)(this,t),Object(s.a)(this,Object(i.a)(t).apply(this,arguments))}return Object(c.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this;return r.a.createElement(E.a,{id:"cardSidebar"},r.a.createElement(y.a,null,r.a.createElement(v.a,{className:"sidebarTulletWrapper",container:!0,direction:"row",justify:"space-between",alignItems:"stretch"},r.a.createElement(v.a,{item:!0,xs:4},r.a.createElement(x.a,{className:" doubleRebondTulletIcon1 sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("tuileDoubleRebond1")[0].getElementsByTagName("input")[0].focus()}},"Tuile Top 1")),r.a.createElement(v.a,{item:!0,xs:4},r.a.createElement(x.a,{className:"doubleRebondTulletIcon2 sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("tuileDoubleRebond2")[0].getElementsByTagName("input")[0].focus()}},"Tuile Top 2")),r.a.createElement(v.a,{item:!0,xs:4},r.a.createElement(x.a,{className:"doubleRebondTulletIcon3 sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("tuileDoubleRebond3")[0].getElementsByTagName("input")[0].focus()}},"Tuile Top 3")),r.a.createElement(v.a,{item:!0,xs:3},r.a.createElement(x.a,{className:"simpleTulletIcon sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("fieldSingle")[0].getElementsByTagName("input")[0].focus()}},"Tuile 1")),r.a.createElement(v.a,{item:!0,xs:3},r.a.createElement(x.a,{className:"simpleTulletIcon sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("fieldSingle")[1].getElementsByTagName("input")[0].focus()}},"Tuile 2")),r.a.createElement(v.a,{item:!0,xs:6},r.a.createElement(x.a,{className:"doubleRebondTulletIcon sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("tuileDoubleRebondOri")[0].getElementsByTagName("input")[0].focus()}},"Double rebond")),r.a.createElement(v.a,{item:!0,xs:3},r.a.createElement(x.a,{className:"simpleTulletIcon sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("fieldSingle")[2].getElementsByTagName("input")[0].focus()}},"Tuile  3")),r.a.createElement(v.a,{item:!0,xs:3},r.a.createElement(x.a,{className:"simpleTulletIcon sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("fieldSingle")[3].getElementsByTagName("input")[0].focus()}},"Tuile 4")),r.a.createElement(v.a,{item:!0,xs:6},r.a.createElement(x.a,{className:"doublesimpleTulletIcon sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("fieldTuileDouble")[0].getElementsByTagName("input")[0].focus()}},"Double")),r.a.createElement(v.a,{item:!0,xs:3},r.a.createElement(x.a,{className:"simpleTulletIcon sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("fieldSingle")[4].getElementsByTagName("input")[0].focus()}},"Tuile 5")),r.a.createElement(v.a,{item:!0,xs:3},r.a.createElement(x.a,{className:"simpleTulletIcon sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("fieldSingle")[5].getElementsByTagName("input")[0].focus()}},"Tuile 6")),r.a.createElement(v.a,{item:!0,xs:3},r.a.createElement(x.a,{className:"simpleTulletIcon sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("fieldSingle")[6].getElementsByTagName("input")[0].focus()}},"Tuile 7")),r.a.createElement(v.a,{item:!0,xs:3},r.a.createElement(x.a,{className:"simpleTulletIcon sidebarTullet noselect",onClick:function(e){document.getElementsByClassName("fieldSingle")[7].getElementsByTagName("input")[0].focus()}},"Tuile 8")))),r.a.createElement("div",{id:"buttonWrapper"},r.a.createElement(R.a,{className:"submitJson",color:"primary",size:"small",variant:"outlined",onClick:function(t){e.props.handleSubmit(t)}}," Valider "),r.a.createElement("div",{id:"cancel"},r.a.createElement(R.a,{className:"reinitJson",color:"secondary",size:"small",variant:"outlined",onClick:function(t){e.props.handleCancel(e.props.handleInputLang)}}," Annuler "),r.a.createElement("p",{id:"warningChange"},"Des Changements sont en cours"))))}}]),t}(r.a.Component),M=a(119),H=a.n(M),L=a(480),W=a(475),A=function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(s.a)(this,Object(i.a)(t).call(this,e))).handleChangeInput=a.handleChangeInput.bind(Object(o.a)(a)),a.handleCancel=a.handleCancel.bind(Object(o.a)(a)),a.handleSubmit=a.handleSubmit.bind(Object(o.a)(a)),a.handleChangeLang=a.handleChangeLang.bind(Object(o.a)(a)),a.hightlight=a.hightlight.bind(Object(o.a)(a)),a.handleTargetBlank=a.handleTargetBlank.bind(Object(o.a)(a)),a.state={lang:"fr",static_double_top:[],single:[],double:"",static_double:{}},a}return Object(c.a)(t,e),Object(l.a)(t,[{key:"handleChangeInput",value:function(e,t,a){if(t||0===t){var n=this.state.single;n[t]=e.target.value,this.setState({single:n})}else if(a){if(Object(b.a)(e.target.parentNode.parentNode.classList).includes("tuileDoubleRebondOri")){var l=this.state.static_double,s=e.target.value;this.setState(function(e){return Object.assign({},e.static_double),l[a]=s,{static_double:l}})}else{var i=Object(b.a)(e.target.parentNode.parentNode.attributes)[1].value,o=e.target.value,c=this.state.static_double_top;this.setState(function(e){return Object.assign(c,e.static_double_top),c[parseInt(i)-1][a]=o,{static_double_top:c}})}}else this.setState({double:e.target.value})}},{key:"handleSubmit",value:function(){var e=this.props.data;"\n        {".concat(this.state.lang,':{\n                "static_double_top":[\n                    {\n                        "image": ').concat(this.state.static_double_top[0].image,',\n                        "link":  ').concat(this.state.static_double_top[0].link,',\n                        "target_blank" : ').concat(this.state.static_double_top.target_blank,'\n                    },{\n                        "image": ').concat(this.state.static_double_top[1].image,',\n                        "link":  ').concat(this.state.static_double_top[1].link,',\n                        "target_blank" : ').concat(this.state.static_double_top.target_blank,'\n                    },{\n                        "image": ').concat(this.state.static_double_top[2].image,',\n                        "link":  ').concat(this.state.static_double_top[2].link,',\n                        "target_blank" : ').concat(this.state.static_double_top.target_blank,'\n                    }\n                ],\n                "single" : ').concat(this.state.single,',\n                "double" : ').concat(this.state.double,',\n                "static_double" : {\n                    "image" : ').concat(this.state.static_double.image,',\n                    "link" : ').concat(this.state.static_double.link,',\n                        "target_blank" : ').concat(this.state.static_double.target_blank,"\n                    }   \n                }\n            }");e[this.state.lang]=this.state,this.updateHomepageData(e)}},{key:"updateHomepageData",value:function(e){fetch("/tma_cms_apps/api/v1/microsite_manager/"+window.props.siteID+"/homepage/",{credentials:"same-origin",method:"PUT",body:JSON.stringify(e),headers:{Accept:"application/json","Content-Type":"application/json","X-CSRFToken":window.csrf}}).then(function(e){return e.json()}).then(function(e){console.log("success"),console.log(e)})}},{key:"handleCancel",value:function(){var e=this;this.setState(function(){return{static_double_top:[Object(g.a)({},e.props.data[e.state.lang].static_double_top[0]),Object(g.a)({},e.props.data[e.state.lang].static_double_top[1]),Object(g.a)({},e.props.data[e.state.lang].static_double_top[2])],single:Object(b.a)(e.props.data[e.state.lang].single),double:e.props.data[e.state.lang].double,static_double:Object(g.a)({},e.props.data[e.state.lang].static_double)}})}},{key:"handleChangeLang",value:function(e,t){var a="";if("en"===t)a="en";else{if("fr"!==t)return;a="fr"}this.setState({lang:a,static_double_top:[Object(g.a)({},this.props.data[a].static_double_top[0]),Object(g.a)({},this.props.data[a].static_double_top[1]),Object(g.a)({},this.props.data[a].static_double_top[2])],single:Object(b.a)(this.props.data[a].single),double:this.props.data[a].double,static_double:Object(g.a)({},this.props.data[a].static_double)})}},{key:"handleTargetBlank",value:function(e){if("original"===e){var t=this.state.static_double;this.setState(function(e){return Object.assign({},e.static_double),e.static_double.target_blank?t.target_blank=!1:t.target_blank=!0,{static_double:t}})}else{var a=this.state.static_double_top;this.setState(function(t){return Object.assign({},t.static_double_top[e-1]),t.static_double_top[e-1].target_blank?a[e-1].target_blank=!1:a[e-1].target_blank=!0,{static_double_top:a}})}}},{key:"hightlight",value:function(e,t){var a=this;for(var n in this.state.single.filter(function(e,t){return a.props.data[a.state.lang].single[t]===e?(document.getElementsByClassName("fieldSingle")[t].getElementsByTagName("input")[0].style.color="",null):(document.getElementsByClassName("fieldSingle")[t].getElementsByTagName("input")[0].style.color="orange",null)}),this.state.double!==this.props.data[this.state.lang].double?document.getElementsByClassName("fieldTuileDouble")[0].getElementsByTagName("input")[0].style.color="orange":document.getElementsByClassName("fieldTuileDouble")[0].getElementsByTagName("input")[0].style.color="",this.state.static_double.image!==this.props.data[this.state.lang].static_double.image?document.getElementsByClassName("tuileDoubleRebondOri")[0].getElementsByTagName("input")[0].style.color="orange":document.getElementsByClassName("tuileDoubleRebondOri")[0].getElementsByTagName("input")[0].style.color="",this.state.static_double.link!==this.props.data[this.state.lang].static_double.link?document.getElementsByClassName("tuileDoubleRebondOri")[1].getElementsByTagName("input")[0].style.color="orange":document.getElementsByClassName("tuileDoubleRebondOri")[1].getElementsByTagName("input")[0].style.color="",this.state.static_double_top)this.state.static_double_top[n].image!==this.props.data[this.state.lang].static_double_top[n].image?document.getElementById("tuileTop").getElementsByClassName("tuileDoubleRebond")[n].getElementsByTagName("input")[0].style.color="orange":document.getElementById("tuileTop").getElementsByClassName("tuileDoubleRebond")[n].getElementsByTagName("input")[0].style.color="",this.state.static_double_top[n].link!==this.props.data[this.state.lang].static_double_top[n].link?document.getElementById("tuileTop").getElementsByClassName("tuileDoubleRebond")[n].getElementsByTagName("input")[1].style.color="orange":document.getElementById("tuileTop").getElementsByClassName("tuileDoubleRebond")[n].getElementsByTagName("input")[1].style.color=""}},{key:"componentDidUpdate",value:function(e,t,a){console.log(t),console.log(t.single.length),0==t.single.length&&(console.log("prevstate vide"),H.a.isEqual(H.a.omit(this.state,["lang"]),this.props.data[this.state.lang])?document.getElementById("cancel").style.display="none":document.getElementById("cancel").style.display="block"),this.hightlight(this.props.data[this.state.lang],H.a.omit(t,["lang","lang"]))}},{key:"componentDidMount",value:function(){this.handleCancel(),console.log(this.state)}},{key:"render",value:function(){return r.a.createElement("div",{className:"wrapper"},this.props.data&&r.a.createElement("div",{id:"mainWrapper"},r.a.createElement(L.a,{value:this.state.lang,indicatorColor:"primary",textColor:"primary",onChange:this.handleChangeLang},r.a.createElement(W.a,{label:"Fr",value:"fr"}),r.a.createElement(W.a,{label:"En",value:"en"})),r.a.createElement("div",{id:"tuileTop"},r.a.createElement(j,{handleTargetBlank:this.handleTargetBlank,handleChangeInput:this.handleChangeInput,keyId:1,static_double:this.state.static_double_top[0],title:"Tuile Top 1"}),r.a.createElement(j,{handleTargetBlank:this.handleTargetBlank,handleChangeInput:this.handleChangeInput,keyId:2,static_double:this.state.static_double_top[1],title:"Tuile Top 2"}),r.a.createElement(j,{handleTargetBlank:this.handleTargetBlank,handleChangeInput:this.handleChangeInput,keyId:3,static_double:this.state.static_double_top[2],title:"Tuile Top 3"})),r.a.createElement(S,{handleChangeInput:this.handleChangeInput,single:this.state.single}),r.a.createElement(j,{handleTargetBlank:this.handleTargetBlank,handleChangeInput:this.handleChangeInput,static_double:this.state.static_double,title:"Tuile double rebond"}),r.a.createElement(D,{handleChangeInput:this.handleChangeInput,double:this.state.double})),r.a.createElement(w,{handleSubmit:this.handleSubmit,handleCancel:this.handleCancel,handleInputLang:this.state.lang}))}}]),t}(r.a.Component),F=a(201),P=a.n(F),J=a(484),z=a(202),U=a(477),q=a(476),G=(a(229),Object(z.a)({palette:{primary:{main:"#5cb7d8"},secondary:q.a},background:"#5cb7d8"})),V=function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(s.a)(this,Object(i.a)(t).call(this,e))).handleHamMenu=a.handleHamMenu.bind(Object(o.a)(a)),a.handleCloseMenu=a.handleCloseMenu.bind(Object(o.a)(a)),a}return Object(c.a)(t,e),Object(l.a)(t,[{key:"handleHamMenu",value:function(e){e.target.previousSibling.style.right="0%"}},{key:"handleCloseMenu",value:function(e){e.target.parentElement.style.right="-45%"}},{key:"render",value:function(){var e=this;return r.a.createElement("div",{className:"header"},r.a.createElement("div",{className:"headWrapper"},r.a.createElement("a",{className:"logo",href:"/"},r.a.createElement("h1",null,r.a.createElement("img",{src:P.a,alt:"Phileas"}))),r.a.createElement("div",{className:"rightSection"},r.a.createElement("a",{className:"explore",href:"/"},"Explorer"),r.a.createElement("div",{className:"closeMenu",onClick:function(t){e.handleCloseMenu(t)}})),r.a.createElement("div",{className:"hamButton",onClick:function(t){e.handleHamMenu(t)}})))}}]),t}(r.a.Component),X=function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(s.a)(this,Object(i.a)(t).call(this,e))).fetchHomepageData=a.fetchHomepageData.bind(Object(o.a)(a)),a.state={data:null,isLoaded:!1},a}return Object(c.a)(t,e),Object(l.a)(t,[{key:"fetchHomepageData",value:function(){var e=this,t={};fetch("/tma_cms_apps/api/v1/microsite_manager/"+window.props.siteID+"/homepage/",{credentials:"same-origin",method:"GET"}).then(function(e){return e.json()}).then(function(a){t=a,e.setState({data:t,isLoaded:!0})})}},{key:"componentDidMount",value:function(){console.log("App did mount"),this.fetchHomepageData()}},{key:"componentDidUpdate",value:function(){console.log("I just updated")}},{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement(V,null),r.a.createElement("h1",{className:"title"},"Administration"),this.state.isLoaded&&r.a.createElement(A,{data:this.state.data}))}}]),t}(r.a.Component);m.a.render(r.a.createElement(U.a,{theme:G},r.a.createElement(J.a,null),r.a.createElement(X,null)),document.getElementById("root"))}},[[209,1,2]]]);
//# sourceMappingURL=main.3888c625.chunk.js.map