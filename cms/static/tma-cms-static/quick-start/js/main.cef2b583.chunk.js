(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{139:function(e,t,a){e.exports=a(186)},144:function(e,t,a){},145:function(e,t,a){},186:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),l=a(11),s=a.n(l),o=(a(144),a(145),a(48)),c=a(20),i=a(21),u=a(23),m=a(22),d=a(24),p=a(193),f=Object(n.createContext)(),g=f.Provider,h=f.Consumer,E=function(e){return function(t){return r.a.createElement(h,null,function(a){return r.a.createElement(e,Object.assign({},a,t))})}},b=a(5),C=a(234),v=a(255),w=a(236),x=function(e){return{IntroStepWrapper:{height:"calc(100vh - 200px)",display:"flex",justifyContent:"center",flexDirection:"column"},stepTitle:{textAlign:"center"},stepHelper:{textAlign:"center"},buttonWrapper:{textAlign:"center",padding:10},createNewBtn:{backgroundColor:window.props.colors.secondColor},createPageWrapper:{padding:"0px 50px 20px 50px"},courseListWrapper:{maxWidth:"800px",margin:"0 auto"},courseElementWrapper:{margin:"20px 0px",borderRadius:10},courseElementtitle:{color:e.palette.primary.main,textTransform:"uppercase"},courseElementInfo:{padding:30},flexCenter:{display:"flex",justifyContent:"center",flexDirection:"column",alignItems:"center"},choseBtn:{borderTopRightRadius:10,borderBottomRightRadius:10,borderBottomLeftRadius:0,borderTopLeftRadius:0,height:"100%",position:"relative",right:"-7px"},dialogButtons:{color:"white!important","&:hover":{color:e.palette.primary.main+"!important"}},bandeau:{backgroundColor:e.palette.primary.main,padding:"30px 50px",color:"white"},bandeauTitle:{fontSize:"1.5rem",margin:0},createCourseWrapper:{padding:20,backgroundColor:"white"},cancelButton:{backgroundColor:"darkgray!important",color:"black",marginLeft:10},disabledBtn:{backgroundColor:"lightgray!important"},backButton:{marginLeft:10},mediumWrapper:{maxWidth:800},smallWrapper:{maxWidth:400},fieldTitle:{color:e.palette.primary.main},fieldWrapper:{padding:"20px 0px"},selectField:{minWidth:400},textEditorWrapper:{marginTop:10,minWidth:800},sliderWrapper:{padding:20},createButtonsWrapper:{padding:20},courseSummaryTitle:{fontWeight:"bold"},loadingPage:{backgroundColor:"white",height:"calc(100vh - 269px)",display:"flex",alignItems:"center",justifyContent:"center",flexDirection:"column"},inputLabel:{marginLeft:10},timeInput:{fontSize:"1rem",textAlign:"right",maxWidth:50,boxShadow:"none",borderRadius:5,padding:5},sideBarTitleWrapper:{padding:25},resetWrapper:{textAlign:"right"},buttonReset:{border:"1px solid lightgray",borderRadius:25,padding:"5px 15px",backgroundColor:"white",fontWeight:"bold",cursor:"pointer"},sideBarTitle:{textAlign:"left",fontWeight:"bold",fontSize:"1rem"},headerWrapper:{marginBottom:25},tabWrapper:{padding:"0px 40px",backgroundColor:"white"},searchWrapper:{padding:"0px 40px"},resultWrapper:{padding:"10px 0px"},resultCard:{borderRadius:15},resultTitle:{color:e.palette.primary.main,margin:0,fontWeight:"initial",textTransform:"uppercase"},actionWrapper:{padding:10,textAlign:"center"},actionStatistics:{backgroundColor:window.props.colors.statisticsColor},actionRerun:{backgroundColor:window.props.colors.mainColor,borderTopRightRadius:15,color:"white",fontWeight:"bold",cursor:"pointer"},actionConfigure:{backgroundColor:window.props.colors.configureColor},actionPreview:{backgroundColor:window.props.colors.secondColor,borderBottomRightRadius:15},actionLink:{textDecoration:"none",color:"white",fontWeight:"bold"},resultInfos:{display:"flex",justifyContent:"center",paddingLeft:25,flexDirection:"column"},tabTitle:{color:"black",textTransform:"Capitalize",fontSize:"1.4rem",fontWeight:"bold"},searchTitle:{color:"black",fontSize:"1rem",fontWeight:"bold"},tabsWrapper:{padding:"20px 50px 0px 50px",backgroundColor:"white"},cartouche:{maxWidth:800,textAlign:"center",backgroundColor:window.props.colors.secondColor,borderRadius:60,color:"white",margin:"0 auto",padding:10},cartoucheTitle:{fontWeight:"bold",margin:0},cartoucheInfo:{margin:0},helpers:{paddingBottom:20},subsections:{padding:"10px 10px",display:"flex",alignItems:"center"},sectionsAdd:{display:"flex",alignItems:"center",padding:"10px 5px",cursor:"pointer",fontWeight:"bold"},clear:{cursor:"pointer",marginLeft:10}}};var y=Object(b.a)(x)(function(e){var t=e.classes;return r.a.createElement(f.Consumer,null,function(e){var a=e.changePage,n=e.page;return r.a.createElement(C.a,{position:"static",className:t.tabWrapper},r.a.createElement(v.a,{value:n,onChange:a,className:t.tabsWrapper},r.a.createElement(w.a,{className:t.tabTitle,label:"Courses"}),r.a.createElement(w.a,{className:t.tabTitle,label:"Vodeclic"})))})}),k=a(237),j=a(39),_=Object(b.a)(function(e){return{appTitle:{textAlign:"left",textTransform:"uppercase",margin:0,display:"inline",fontSize:"1.3rem"},appTitleWrapper:{backgroundColor:"white",padding:"30px 50px",display:"flex",alignItems:"center",justifyContent:"space-between"},quickStartWrapper:{display:"inline"},"@global":{header:{boxShadow:"none!important"},a:{textDecoration:"none",color:"initial"}}}})(function(e){function t(){return Object(c.a)(this,t),Object(u.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e=this.props.classes;return r.a.createElement("div",{className:e.appTitleWrapper},r.a.createElement("h1",{className:e.appTitle},r.a.createElement(j.b,{to:"/"},"Accueil Studio")),r.a.createElement("div",{className:e.quickStartWrapper},r.a.createElement(j.b,{to:"/create"},r.a.createElement(k.a,null,"Quick start"))))}}]),t}(n.Component));var N=Object(b.a)(x)(function(e){var t=e.classes;return r.a.createElement("div",{className:t.headerWrapper},r.a.createElement(_,null),r.a.createElement(y,null))}),O=a(242),W=a(122),F=a(238),T=a(187),S=a(239),D=a(257),B=function(e){function t(){return Object(c.a)(this,t),Object(u.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e=this.props,t=e.filter,a=e.selectOption,n=this.props.selectedFilters?this.props.selectedFilters[t.name]:void 0;return r.a.createElement("div",null,r.a.createElement(F.a,{component:"fieldset"},r.a.createElement(T.a,null,t.options.map(function(e,l){return r.a.createElement(S.a,{key:l,control:r.a.createElement(D.a,{checked:!(!n||!n.includes(e)),value:e,id:e,onClick:function(n){return a(n,t.name,e)}}),label:e,style:{marginTop:0,marginBottom:0}})}))))}}]),t}(n.Component),I=E(Object(b.a)(function(e){return{container:{paddingTop:35}}})(B)),R=a(260),L=a(240),A=a(241),P=Object(b.a)({root:{border:"0px",borderTop:"1px solid lightgray",boxShadow:"none","&:not(:last-child)":{borderBottom:0},"&:before":{display:"none"},"&$expanded":{margin:"auto"}},expanded:{}})(R.a),z=Object(b.a)({root:{backgroundColor:"white",borderBottom:"0px",marginBottom:-1,paddingRight:0,minHeight:56,"&$expanded":{minHeight:56}},content:{"&$expanded":{margin:"12px 0"}},expanded:{}})(L.a),q=Object(b.a)(function(e){return{root:{padding:e.spacing(2)}}})(A.a),M=function(e){function t(){var e,a;Object(c.a)(this,t);for(var n=arguments.length,l=new Array(n),s=0;s<n;s++)l[s]=arguments[s];return(a=Object(u.a)(this,(e=Object(m.a)(t)).call.apply(e,[this].concat(l)))).state={open:!1},a.buildFilterOptions=function(e){if("checkbox"===e.type)return r.a.createElement(I,{filter:e})},a.toggleOpen=function(){a.setState(function(e){return{open:!e.open}})},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e=this.props,t=e.filter,a=e.classes,n=this.state.open;return r.a.createElement(P,null,r.a.createElement(z,{onClick:this.toggleOpen},r.a.createElement(O.a,{container:!0},r.a.createElement(O.a,{item:!0,xs:10},r.a.createElement("h5",{className:a.filterTitle},t.name)),r.a.createElement(O.a,{item:!0,xs:2},r.a.createElement("span",{className:a.closeBtn},n?"-":"+")))),r.a.createElement(q,null,"\xa0",this.buildFilterOptions(t)))}}]),t}(n.Component),H=Object(b.a)(function(e){return{filterTitle:{fontWeight:"bold",color:"lightgray",textTransform:"uppercase",fontSize:"1rem",margin:0},closeBtn:{backgroundColor:e.palette.primary.main,color:"white",padding:"0px 5px",borderRadius:5,display:"inline-block",minWidth:20,textAlign:"center"}}})(M);var U=Object(b.a)(x)(function(e){var t=e.classes;return r.a.createElement(f.Consumer,null,function(e){var a=e.filters,n=e.resetFilters;return r.a.createElement(W.a,{className:t.sideBarWrapper},r.a.createElement("div",{className:t.sideBarTitleWrapper},r.a.createElement("div",{className:t.resetWrapper},r.a.createElement("button",{className:t.buttonReset,onClick:function(){return n()}},"Reset")),r.a.createElement("p",{className:t.sideBarTitle},"Add filter"),r.a.createElement("p",null,"Select filters you want for your search")),r.a.createElement("div",null,a.map(function(e,t){return r.a.createElement(H,{key:t,filter:e})})))})}),V=a(94),$=Object(b.a)(x)(function(e){var t=e.title,a=e.resultList,n=e.classes,l=e.page;return r.a.createElement("div",{className:n.searchWrapper},r.a.createElement(V.a,{component:"div",className:n.searchTitle},t),void 0!==a&&a.map(function(e,t){return r.a.createElement(J,{key:t,result:e})}),"base"!==l&&void 0!==a&&0===a.length&&r.a.createElement("p",null,"No results"))}),J=Object(b.a)(x)(function(e){var t=e.result,a=e.classes;return r.a.createElement("div",{className:a.resultWrapper},r.a.createElement(W.a,{className:a.resultCard},r.a.createElement(O.a,{container:!0},r.a.createElement(O.a,{item:!0,xs:9,className:a.resultInfos},r.a.createElement("h2",{className:a.resultTitle},t.course_name),r.a.createElement("p",null,t.course_id)),r.a.createElement(O.a,{item:!0,xs:3},r.a.createElement(j.b,{to:"/quick-start/"+t.course_id},r.a.createElement("div",{className:[a.actionWrapper,a.actionRerun].join(" ")},r.a.createElement("span",null,"Re-run course"))),r.a.createElement("div",{className:[a.actionWrapper,a.actionConfigure].join(" ")},r.a.createElement("a",{className:a.actionLink,href:t.configure_url},r.a.createElement("span",null,"Configure"))),r.a.createElement("div",{className:[a.actionWrapper,a.actionStatistics].join(" ")},r.a.createElement("a",{className:a.actionLink,href:t.stats_url},r.a.createElement("span",null,"Statistics"))),r.a.createElement("div",{className:[a.actionWrapper,a.actionPreview].join(" ")},r.a.createElement("a",{className:a.actionLink,href:t.preview_url},r.a.createElement("span",null,"Live preview")))))))}),G=E(function(e){function t(){var e,a;Object(c.a)(this,t);for(var n=arguments.length,r=new Array(n),l=0;l<n;l++)r[l]=arguments[l];return(a=Object(u.a)(this,(e=Object(m.a)(t)).call.apply(e,[this].concat(r)))).respectFilters=function(e,t){var a=[];return Object.entries(t).forEach(function(t){var n=!1,r=t[0],l=t[1];l.includes("all")?n=!0:Array.isArray(e[r])?e[r].forEach(function(e){l.includes(e)&&(n=!0)}):l.includes(e[r])&&(n=!0),a.push(n)}),!a.includes(!1)},a.filterResults=function(e,t,n){return 0===t?e.filter(function(e){return"phileas"===e.type&&a.respectFilters(e,n)}):1===t?e.filter(function(e){return"vodeclic"===e.type&&a.respectFilters(e,n)}):[]},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e=this.props,t=e.page,a=e.selectedFilters;console.log(t);var n=this.filterResults(window.props.courses,t,a);return r.a.createElement("div",null,0===Object.entries(a).length&&r.a.createElement($,{page:"base",title:"Choose filters and start research to find all the courses"}),Object.entries(a).length>0&&0===t&&r.a.createElement($,{title:"Courses results",resultList:n,page:0}),Object.entries(a).length>0&&1===t&&r.a.createElement($,{title:"Vodeclic results",resultList:n,page:1}))}}]),t}(n.Component)),K=function(e){function t(){var e,a;Object(c.a)(this,t);for(var n=arguments.length,r=new Array(n),l=0;l<n;l++)r[l]=arguments[l];return(a=Object(u.a)(this,(e=Object(m.a)(t)).call.apply(e,[this].concat(r)))).state={page:0,selectedFilters:[],filters:window.props.filters,translations:window.props.translations,colors:window.props.colors},a.getContext=function(){return Object(o.a)({},a.state,{changePage:a.changePage,selectOption:a.selectOption,resetFilters:a.resetFilters})},a.changePage=function(e,t){a.setState({page:t})},a.resetFilters=function(){a.setState({selectedFilters:[]}),console.log("hello")},a.selectOption=function(e,t,n){e.stopPropagation();var r=a.state.selectedFilters;r&&r[t]?r[t].includes(n)?(r[t]=r[t].filter(function(e){return e!==n}),0===r[t].length&&delete r[t]):r[t].push(n):r[t]=[n],a.setState({selectedFilters:r})},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e=this.props.classes;return r.a.createElement(n.Fragment,null,r.a.createElement(g,{value:this.getContext()},r.a.createElement(N,null),r.a.createElement(O.a,{container:!0,className:e.container},r.a.createElement(O.a,{item:!0,md:3,xs:12},r.a.createElement(U,null)),r.a.createElement(O.a,{item:!0,md:9,xs:12},r.a.createElement(G,{page:this.state.page})))))}}]),t}(n.Component),Q=Object(p.a)(function(e){return{}})(K),Z=a(64),X=a.n(Z),Y=a(90),ee=a(58),te=Object(p.a)(x)(function(e){var t=e.classes,a=e.setMode;return r.a.createElement("div",{className:t.IntroStepWrapper},r.a.createElement("h1",{className:t.stepTitle},"Quick Start"),r.a.createElement("p",{className:t.stepHelper},"Choose the way you want to create a course"),r.a.createElement("div",{className:t.buttonWrapper},r.a.createElement(k.a,{onClick:function(e){return a("re-run")}},"Start from an existing course")),r.a.createElement("div",{className:t.buttonWrapper},r.a.createElement(k.a,{className:t.createNewBtn,onClick:function(e){return a("new-course")}},"Create new course")))}),ae=Object(p.a)(x)(function(e){var t=e.classes,a=e.course,n=e.setCourse;return r.a.createElement(W.a,{className:t.courseElementWrapper},r.a.createElement(O.a,{container:!0},r.a.createElement(O.a,{item:!0,xs:9,className:t.courseElementInfo},r.a.createElement(V.a,{className:t.courseElementtitle},a.course_name),r.a.createElement(V.a,null,a.course_id)),r.a.createElement(O.a,{item:!0,xs:3,className:t.flexCenter},r.a.createElement(k.a,{className:t.choseBtn,onClick:function(e){return n(a)}},r.a.createElement(V.a,null,"Choose this course")))))}),ne=Object(p.a)(x)(function(e){var t=e.courses,a=e.classes,n=e.setCourse;return r.a.createElement("div",null,r.a.createElement("h1",{className:a.stepTitle},"Course-Rerun"),r.a.createElement("p",{className:a.stepHelper},"Select a Course :"),r.a.createElement("div",{className:a.courseListWrapper},t.map(function(e,t){return r.a.createElement(ae,{course:e,key:t,setCourse:n})})))}),re=a(42),le=a(256),se=a(258),oe=a(249),ce=a(248),ie=a(119),ue=a(84),me=a(261),de=a(254),pe=a(250),fe=a(91),ge=a.n(fe),he=a(121),Ee=a(93),be=a.n(Ee),Ce=a(92),ve=a.n(Ce),we=Object(b.a)(x)(function(e){var t=e.field,a=e.translations,n=e.classes,l=e.addCourseDetails,s=e.value;return r.a.createElement("div",{className:n.mediumWrapper+" "+n.fieldWrapper},r.a.createElement("h3",{className:n.fieldTitle},a.stepFields[t.name+"_title"]),r.a.createElement("p",null,a.stepFields[t.name+"_helper"]),r.a.createElement(O.a,{container:!0,direction:"row",justify:"center",alignItems:"center"},r.a.createElement(O.a,{item:!0,xs:6},r.a.createElement(he.a,{onChange:function(e){return a=e,void l({name:t.name,value:a});var a},filesLimit:1,acceptedFiles:["image/*"],dropzoneText:a.dragAndDropInfo,showAlerts:!1,showPreviewsInDropzone:!0})),r.a.createElement(O.a,{item:!0,xs:6},s&&s[0]&&r.a.createElement("img",{style:{maxWidth:"100%",padding:20},src:URL.createObjectURL(s[0]),alt:"course illustration"}))))}),xe=Object(b.a)(x)(function(e){var t=e.field,a=e.translations,n=e.classes,l=e.addCourseDetails,s=e.value,o=function(e,a){console.log("change",a,t.name),l("hours"===e?{name:t.name,value:[a,s[1]]}:{name:t.name,value:[s[0],a]})};return r.a.createElement(r.a.Fragment,null,r.a.createElement("div",{className:[n.fieldWrapper,n.smallWrapper].join(" ")},r.a.createElement("h3",{className:n.fieldTitle},a.stepFields[t.name+"_title"]),r.a.createElement("p",null,a.stepFields[t.name+"_helper"]),r.a.createElement(O.a,{container:!0},r.a.createElement(O.a,{item:!0,xs:6},r.a.createElement(ge.a,{value:s[0],onChange:function(e){return o("hours",e.target.value)},className:n.timeInput}),r.a.createElement("span",{className:n.inputLabel},a.hours)),r.a.createElement(O.a,{item:!0,xs:6},r.a.createElement(ge.a,{value:s[1],onChange:function(e){return o("minutes",e.target.value)},className:n.timeInput}),r.a.createElement("span",{className:n.inputLabel},a.minutes)))))}),ye=Object(b.a)(x)(function(e){var t=e.field,a=e.translations,n=e.defaultValue,l=e.handleFieldChange,s=e.fixedField,o=e.classes,c=e.newCourse,i=["course_session","course_number"].includes(t.name)&&!c.validCourseId;return r.a.createElement(r.a.Fragment,null,r.a.createElement("h3",{className:o.fieldTitle},a.stepFields[t.name+"_title"],t.required&&"*"),r.a.createElement("p",null,a.stepFields[t.name+"_helper"])," ",s&&r.a.createElement("p",null,a.stepFields.rerunWarning),r.a.createElement(le.a,{defaultValue:a.stepFields[t.name+"_default_value"],margin:"normal",value:n,InputProps:s?{readOnly:!0}:{},onChange:function(e){return l(t.name,e.target.value)},variant:"outlined",error:i}),i&&r.a.createElement(ce.a,{error:!0,id:"component-error-text"},a.invalidCourseId," "))}),ke=Object(b.a)(x)(function(e){var t=e.field,a=e.translations,n=e.classes,l=e.addCourseDetails,s=e.value;return r.a.createElement("div",{className:n.fieldWrapper},r.a.createElement("h3",{className:n.fieldTitle},a.stepFields[t.name+"_title"]),r.a.createElement("p",null,a.stepFields[t.name+"_helper"]),r.a.createElement(F.a,{component:"fieldset"},r.a.createElement(oe.a,{"aria-label":t.name,name:t.name,value:s||t.options[0],onChange:(t.name,function(e){l({value:e.target.value,name:t.name})})},t.options.map(function(e,t){return r.a.createElement("div",{key:t},r.a.createElement(S.a,{value:e,control:r.a.createElement(se.a,null),label:a.stepFields[e+"_title"]||e}),r.a.createElement(ce.a,null,a.stepFields[e+"_helper"]))}))))}),je=Object(b.a)(x)(function(e){var t=e.field,a=e.translations,n=e.classes,l=e.addCourseDetails,s=e.value;return r.a.createElement("div",{className:n.fieldWrapper},r.a.createElement("h3",{className:n.fieldTitle},a.stepFields[t.name+"_title"]),r.a.createElement("p",null,a.stepFields[t.name+"_helper"]),r.a.createElement(F.a,{component:"fieldset"},r.a.createElement(T.a,null,t.options.map(function(e,t){return r.a.createElement("div",{key:t},r.a.createElement(S.a,{control:r.a.createElement(D.a,{value:e,onChange:(n=e,function(e){l({name:n,value:e.target.checked})}),checked:s[e]}),label:a.stepFields[e+"_title"]||e}),r.a.createElement(ce.a,null,a.stepFields[e+"_helper"]));var n}))))});function _e(e){var t=e.type,a=e.translations,n=e.value,l=e.addCourseDetails;function s(e){l({value:e,name:t})}return r.a.createElement(ue.c,{utils:ie.a},r.a.createElement(O.a,{container:!0,justify:"space-around"},r.a.createElement(ue.a,{margin:"normal",id:"mui-pickers-date",label:"startDate"===t?a.startDate_date:a.endDate_date,value:n,onChange:s,KeyboardButtonProps:{"aria-label":"change date"},cancelLabel:a.cancel,okLabel:a.confirm}),r.a.createElement(ue.b,{margin:"normal",id:"mui-pickers-time",label:"startDate"===t?a.startDate_time:a.endDate_time,value:n,onChange:s,KeyboardButtonProps:{"aria-label":"change time"},cancelLabel:a.cancel,okLabel:a.confirm})))}var Ne=Object(b.a)(x)(function(e){var t=e.value,a=void 0===t?"":t,n=e.field,l=e.translations,s=e.classes,o=e.addCourseDetails;return r.a.createElement("div",{className:s.fieldWrapper},r.a.createElement("h3",{className:s.fieldTitle},l.stepFields[n.name+"_title"]),r.a.createElement(ce.a,null,l.stepFields[n.name+"_helper"]),r.a.createElement(F.a,{variant:"outlined"},r.a.createElement(de.a,{value:a,onChange:function(e){o({value:e.target.value,name:n.name})},inputProps:{name:n.name},className:s.selectField},r.a.createElement(me.a,{value:""},r.a.createElement("em",null)),n.options.map(function(e,t){return r.a.createElement(me.a,{key:t,value:e},l.stepFields[e+"_title"]||e)}))))}),Oe=Object(b.a)(x)(function(e){var t=e.value,a=e.field,n=e.translations,l=e.classes,s=e.addCourseDetails;return r.a.createElement("div",{className:l.fieldWrapper},r.a.createElement("h3",{className:l.fieldTitle},n.stepFields[a.name+"_title"]),r.a.createElement(ce.a,null,n.stepFields[a.name+"_helper"]),r.a.createElement(le.a,{rows:"4",className:l.textEditorWrapper,multiline:!0,variant:"outlined",onChange:function(e){s({value:e.target.value,name:a.name})},value:t}))}),We=Object(b.a)({thumb:{height:24,width:24,backgroundColor:"#fff",marginTop:10},track:{backgroundColor:window.props.colors.configureColor,height:24,borderRadius:60},trackAfter:{backgroundColor:window.props.colors.statisticsColor,opacity:1,borderRadius:60},container:{height:70}})(pe.a),Fe=Object(b.a)(x)(function(e){var t=e.value,a=e.field,n=e.translations,l=e.classes,s=e.addCourseDetails;return r.a.createElement("div",{className:l.fieldWrapper},r.a.createElement("h3",{className:l.fieldTitle},n.stepFields[a.name+"_title"]),r.a.createElement(ce.a,null,n.stepFields[a.name+"_helper"]),r.a.createElement("p",null,n.fail||"Fail Level"," : 0% - ",Math.round(t),"% "),r.a.createElement("p",null,n.pass||"Pass"," : ",Math.round(t),"% - 100% "),r.a.createElement(We,{container:{height:60},value:t,onChange:function(e,t){s({value:Math.round(t),name:a.name})},className:l.sliderWrapper}),r.a.createElement(O.a,{container:!0,direction:"row",justify:"space-between",alignItems:"center"},function(){for(var e=[],t=0;t<=100;t+=10)e.push(r.a.createElement("span",{key:t},t));return e}()))}),Te=Object(b.a)(x)(function(e){var t=e.classes,a=e.value,n=e.field,l=e.translations,s=e.addCourseDetails,o=function(e,t){var r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:void 0,l=Object(re.a)(a);void 0!==r?l[t].subsections[r]=e:l[t].title=e,s({name:n.name,value:l})},c=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:void 0,r=Object(re.a)(a);void 0!==t?r[e].subsections.length>1?r[e].subsections=[].concat(Object(re.a)(r[e].subsections.splice(0,t)),Object(re.a)(r[e].subsections.splice(t+1))):r[e].subsections=[]:r=[].concat(Object(re.a)(r.splice(0,e)),Object(re.a)(r.splice(e+1))),s({name:n.name,value:r})};return r.a.createElement("div",{className:t.fieldWrapper},r.a.createElement("h3",{className:t.fieldTitle},l.stepFields[n.name+"_title"]),r.a.createElement(ce.a,{className:t.helpers},l.stepFields[n.name+"_helper"]),r.a.createElement(O.a,{container:!0,direction:"column",justify:"center",alignItems:"flex-start",spacing:2},a.map(function(e,i){return r.a.createElement("div",{key:i},r.a.createElement(O.a,{item:!0},r.a.createElement(le.a,{value:e.title,variant:"outlined",onChange:function(e){return o(e.target.value,i)}}),r.a.createElement(ve.a,{className:t.clear,onClick:function(){return c(i)}})),e.subsections.map(function(e,a){return r.a.createElement(O.a,{item:!0,key:a,className:t.subsections},r.a.createElement(le.a,{value:e,variant:"outlined",onChange:function(e){return o(e.target.value,i,a)}}),r.a.createElement(ve.a,{className:t.clear,onClick:function(){return c(i,a)}}))}),r.a.createElement("span",{className:t.sectionsAdd,onClick:function(e){return function(e){var t=Object(re.a)(a);t[e].subsections.push(l.new_subsection||"New subsection"),s({name:n.name,value:t})}(i)}},r.a.createElement(be.a,null)," ",l.addSubsection||"Add Subsection"))}),r.a.createElement("span",{className:t.sectionsAdd,onClick:function(){s({name:n.name,value:[].concat(Object(re.a)(a),[{title:l.new_section||"New Section",subsections:[l.new_subsection||"New Subsection"]}])})}},r.a.createElement(be.a,null)," ",l.addSection||"Add Section")))}),Se=Object(b.a)(x)(function(e){var t=e.classes;return r.a.createElement(f.Consumer,null,function(e){var a=e.newCourse,n=e.translations;return r.a.createElement("div",{className:t.cartouche},r.a.createElement(O.a,{container:!0,direction:"row",justify:"center",alignItems:"center"},r.a.createElement(O.a,{item:!0,xs:3},r.a.createElement("p",{className:t.cartoucheTitle},n.stepFields.course_name_title),r.a.createElement("p",{className:t.cartoucheInfo},a.course_name)),r.a.createElement(O.a,{item:!0,xs:3},r.a.createElement("p",{className:t.cartoucheTitle},n.stepFields.org_title),r.a.createElement("p",{className:t.cartoucheInfo},a.org)),r.a.createElement(O.a,{item:!0,xs:3},r.a.createElement("p",{className:t.cartoucheTitle},n.stepFields.course_number_title),r.a.createElement("p",{className:t.cartoucheInfo},a.course_number)),r.a.createElement(O.a,{item:!0,xs:3},r.a.createElement("p",{className:t.cartoucheTitle},n.stepFields.course_session_title),r.a.createElement("p",{className:t.cartoucheInfo},a.course_session))))})}),De=a(115),Be=a.n(De);a(164);var Ie=function(e){var t=e.newCourse,a=e.translations,n=e.classes;return r.a.createElement("div",null,r.a.createElement("h3",null,a.verifyCourseInfo),Object.entries(t).map(function(e,l){return r.a.createElement("div",{key:l},function(e){var l;if(l=e[1]instanceof Date?r.a.createElement(Be.a,{locale:"fr"===window.props.currentLanguage?"fr":"en",format:"LLL"},e[1].toString()):"course_grade"===e[0]?t.is_course_graded?r.a.createElement("span",null,e[1],"%"):r.a.createElement("span",null,a.courseNotGraded):"effort"===e[0]?r.a.createElement("span",null," ",e[1][0]," ",a.hours," ",e[1][1]," ",a.minutes," "):"course_image"===e[0]?e[1]?r.a.createElement("div",null,r.a.createElement("img",{style:{maxWidth:150},src:URL.createObjectURL(e[1][0]),alt:"course illustration"})):r.a.createElement("span",null,a.noImage):"teacher_image"===e[0]?e[1]?r.a.createElement("div",null,r.a.createElement("img",{style:{maxWidth:150},src:URL.createObjectURL(e[1][0]),alt:"teacher illustration"})):r.a.createElement("span",null,a.noImage):"course_map"===e[0]?e[1]?e[1].map(function(e){return r.a.createElement(r.a.Fragment,null,r.a.createElement("p",null,e.title),e.subsections.map(function(e){return r.a.createElement("p",null,e)}))}):r.a.createElement("span",null,a.no_course_map||"No course map provided"):"boolean"===typeof e[1]?r.a.createElement("span",null,a[e[1].toString()]):r.a.createElement("span",null,a.stepFields[e[1]+"_title"]||e[1]))return r.a.createElement(r.a.Fragment,null,r.a.createElement("span",{className:n.courseSummaryTitle},a.stepFields[e[0]+"_title"]||e[0]," : "),l)}(e))}))},Re=a(116),Le=a.n(Re),Ae=a(117),Pe=a.n(Ae),ze=a(118),qe=a.n(ze);var Me=Object(p.a)(x)(function(e){var t=e.classes;return r.a.createElement(f.Consumer,null,function(e){var a=e.newCourseResponse,n=e.translations;return r.a.createElement("div",{className:t.loadingPage},a?r.a.createElement(He,null):r.a.createElement(r.a.Fragment,null,r.a.createElement("h3",null,n.waitCourseCreation),r.a.createElement(Le.a,{type:"Puff",color:window.props.colors.mainColor,height:"100",width:"100"})))})}),He=function(e){return r.a.createElement(f.Consumer,null,function(e){var t=e.newCourseResponse,a=e.newCourse,n=e.eraseNewCourse,l=e.translations;return r.a.createElement(r.a.Fragment,null,"error"!==t.status?r.a.createElement(r.a.Fragment,null,r.a.createElement("div",null,r.a.createElement(Pe.a,{style:{fontSize:90,color:window.props.colors.mainColor}})),r.a.createElement("h3",null,l.courseHasBeenCreated),r.a.createElement("h4",null,l.stepFields.course_name_title," : ",a.course_name),r.a.createElement(O.a,{container:!0,spacing:6,direction:"row",justify:"center",alignItems:"center"},r.a.createElement(O.a,{item:!0},r.a.createElement(k.a,{href:t.edit_link,onClick:function(){return n()}},l.seeMyCourse)),r.a.createElement(O.a,{item:!0},r.a.createElement(j.b,{to:"/"},r.a.createElement(k.a,{onClick:function(){return n()}},l.backToHomePage))))):r.a.createElement(r.a.Fragment,null,r.a.createElement("div",null,r.a.createElement(qe.a,{style:{fontSize:90,color:"red"}})),r.a.createElement("h3",null,l.errorWhileCreatingCourse),r.a.createElement("h4",null,l.courseNotCreated),r.a.createElement(O.a,{container:!0,spacing:6,direction:"row",justify:"center",alignItems:"center"},r.a.createElement(O.a,{item:!0},r.a.createElement(j.b,{to:"/"},r.a.createElement(k.a,{onClick:function(){return n()}},l.backToHomePage))))))})},Ue=function(e){function t(){var e,a;Object(c.a)(this,t);for(var n=arguments.length,l=new Array(n),s=0;s<n;s++)l[s]=arguments[s];return(a=Object(u.a)(this,(e=Object(m.a)(t)).call.apply(e,[this].concat(l)))).state={step1:[{name:"course_name",required:!0,type:"text"},{name:"org",required:!0,type:"text"},{name:"course_number",required:!0,type:"text"},{name:"course_session",required:!0,type:"text"}],step2:[{name:"course_pacing",type:"radio",options:["instructor_paced","self_paced"]},{name:"effort",type:"time"},{name:"course_dates",type:"date"},{name:"language",type:"select",options:["fr","en","de","es","it"]},{name:"course_type",type:"checkBox",options:["is_invitation_only","is_manager_only","is_mandatory"]}],step3:[{name:"course_tag",type:"select",options:["computer science","finance","management","desktop","design"]},{name:"course_onboarding_tag",type:"select",options:["onboarding_1","onboarding_2","onboarding_3"]},{name:"course_image",type:"image"},{name:"course_about",type:"textField"},{name:"course_map",type:"jsonEditor"},{name:"teacher_image",type:"image"},{name:"teacher_name",required:!1,type:"text"},{name:"teacher_email",required:!1,type:"text"}],step4:[{name:"course_settings",type:"checkBox",options:["is_course_graded","has_menu"]},{name:"course_grade",type:"grade"}]},a.createFields=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},n=a.context,l=n.handleFieldChange,s=n.newCourse,o=n.translations,c=n.addCourseDetails,i=a.props.classes;return e.map(function(e,a){switch(e.type){case"text":return r.a.createElement(ye,{key:a,field:e,translations:o,defaultValue:s[e.name]||"",handleFieldChange:l,fixedField:t[e.name]&&!0,newCourse:s});case"radio":return r.a.createElement(ke,{key:a,field:e,translations:o,addCourseDetails:c,value:s[e.name]});case"checkBox":return r.a.createElement(je,{key:a,field:e,translations:o,addCourseDetails:c,value:s});case"date":return r.a.createElement("div",{key:a,className:i.mediumWrapper+" "+i.fieldWrapper},r.a.createElement("h3",{className:i.fieldTitle},o.stepFields.course_dates_title),r.a.createElement("p",null,o.stepFields.course_dates_title_helper),r.a.createElement(_e,{type:"startDate",addCourseDetails:c,translations:o,value:s.startDate}),r.a.createElement(_e,{type:"endDate",addCourseDetails:c,translations:o,value:s.endDate}));case"select":return r.a.createElement(Ne,{key:a,field:e,translations:o,addCourseDetails:c,value:s[e.name]});case"textField":return r.a.createElement(Oe,{key:a,field:e,translations:o,addCourseDetails:c,value:s[e.name]});case"grade":return r.a.createElement(Fe,{key:a,field:e,translations:o,addCourseDetails:c,value:s[e.name]});case"time":return r.a.createElement(xe,{key:a,field:e,translations:o,addCourseDetails:c,value:s[e.name]||[]});case"image":return r.a.createElement(we,{key:a,field:e,translations:o,addCourseDetails:c,value:s[e.name]});case"jsonEditor":return r.a.createElement(Te,{key:a,field:e,value:s[e.name],translations:o,addCourseDetails:c});default:return""}})},a.validCourseParameters=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[],t=!0,n=a.context.newCourse;return e.forEach(function(e){e.required&&!n[e.name]&&(t=!1)}),t},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e=this.context,t=e.step,a=e.mode,n=e.selectedCourse,l=e.translations,s=e.handleNextClick,o=e.newCourse,c=e.toggleDialog,i=e.handleBackClick,u=e.launchCourseCreation,m=e.checkCourseId,d=this.props.classes,p=this.state["step"+t],f=!this.validCourseParameters(p);return r.a.createElement(r.a.Fragment,null,r.a.createElement("div",{className:d.bandeau},[1,2,3,4].includes(t)?r.a.createElement(V.a,null,"Step ",t,"/4"):r.a.createElement("h3",{className:d.bandeauTitle},l.stepFields.courseSummary),r.a.createElement("h3",{className:d.bandeauTitle},"Create Course - Mode ",a)),r.a.createElement("div",{className:d.createCourseWrapper},[2,3,4].includes(t)&&r.a.createElement(Se,{translations:l,newCourse:o}),[1,2,3,4].includes(t)&&this.createFields(p,n),5===t&&r.a.createElement(Ie,{newCourse:o,translations:l,classes:d}),6===t&&r.a.createElement(Me,{classes:d,translations:l})),[1,2,3,4,5].includes(t)&&r.a.createElement("div",{className:d.createButtonsWrapper},1===t&&r.a.createElement(k.a,{disabled:f,onClick:function(){return m()},className:f?d.disabledBtn:""},l.next),[2,3,4].includes(t)&&r.a.createElement(k.a,{disabled:f,onClick:function(){return s()}},l.next),5===t&&r.a.createElement(k.a,{disabled:f,onClick:function(e){return u(e)}},l.createCourse),[2,3,4,5].includes(t)&&r.a.createElement(k.a,{onClick:function(){return i()},className:d.backButton},l.back),r.a.createElement(k.a,{className:d.cancelButton,onClick:function(){return c()}},l.cancel)))}}]),t}(n.Component);Ue.contextType=f;var Ve=Object(b.a)(x)(Ue),$e=a(259),Je=a(245),Ge=a(244),Ke=a(251),Qe=a(243);var Ze=Object(p.a)(x)(function(e){var t=e.openDialog,a=e.toggleDialog,n=e.dialogTitle,l=e.dialogContent,s=e.dialogValid,o=e.dialogCancel,c=e.dialogAction,i=e.classes;return r.a.createElement("div",null,r.a.createElement($e.a,{open:t,onClose:a,"aria-labelledby":"alert-dialog-title","aria-describedby":"alert-dialog-description"},r.a.createElement(Qe.a,{id:"alert-dialog-title"},n),r.a.createElement(Ge.a,null,r.a.createElement(Ke.a,{id:"alert-dialog-description"},l)),r.a.createElement(Je.a,null,s&&r.a.createElement(k.a,{onClick:c,color:"primary",className:i.dialogButtons},s),o&&r.a.createElement(k.a,{onClick:a,color:"primary",autoFocus:!0,className:i.dialogButtons},o))))}),Xe=window.props.courseBasis,Ye=function(e){function t(){var e,a;Object(c.a)(this,t);for(var n=arguments.length,r=new Array(n),l=0;l<n;l++)r[l]=arguments[l];return(a=Object(u.a)(this,(e=Object(m.a)(t)).call.apply(e,[this].concat(r)))).state={translations:window.props.translations,courses:window.props.courses||[],step:0,selectedCourse:void 0,mode:"new-course",newCourse:Xe,cancelCreationPopup:!1,newCourseResponse:void 0},a.setMode=function(e){a.setState(function(t){return{mode:e,step:t.step+1}})},a.setCourse=function(e){a.setState(function(t){return{selectedCourse:e,newCourse:Object(o.a)({},t.newCourse,{course_name:e.course_name,org:e.org})}})},a.addCourseDetails=function(e){a.setState(function(t){return{newCourse:Object(o.a)({},t.newCourse,Object(ee.a)({},e.name,e.value))}})},a.handleNextClick=function(){a.setState(function(e){return{step:e.step+1}})},a.checkCourseId=Object(Y.a)(X.a.mark(function e(){var t,n,r,l,s,c;return X.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return t=a.state.newCourse,n=window.props.api.courseidChecking+"course-v1:"+t.org.toString()+"+"+t.course_number.toString()+"+"+t.course_session.toString(),r={method:"GET",headers:{Accept:"application/json","Content-Type":"application/json"}},e.next=5,fetch(n,r);case 5:return l=e.sent,e.next=8,l.json();case 8:return s=e.sent,c="valid_new_id"===s.details,a.setState(function(e){return{newCourse:Object(o.a)({},e.newCourse,{validCourseId:c})}}),c&&a.handleNextClick(),e.abrupt("return");case 13:case"end":return e.stop()}},e)})),a.launchCourseCreation=function(){var e=Object(Y.a)(X.a.mark(function e(t){var n,r,l,s;return X.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return t.preventDefault(),a.handleNextClick(),n=window.props.api.courseCreationUrl,r={method:"POST",body:a.getFormData(),contentType:!1,processData:!1},e.next=6,fetch(n,r);case 6:return l=e.sent,e.next=9,l.json();case 9:"404"!==(s=e.sent).cod&&a.setState({newCourseResponse:s});case 11:case"end":return e.stop()}},e)}));return function(t){return e.apply(this,arguments)}}(),a.getCourseEffort=function(){return(3600*a.state.newCourse.effort[0]||0)+(60*a.state.newCourse.effort[1]||0)},a.getFormData=function(){var e=new FormData;return Object.entries(a.state.newCourse).forEach(function(t){console.log(t),"course_image"===t[0]&&t[1]?e.append("course_image",a.state.newCourse.course_image[0]):"teacher_image"===t[0]&&t[1]?e.append("teacher_image",a.state.newCourse.teacher_image[0]):"effort"===t[0]?e.append("effort",a.getCourseEffort()):"course_map"===t[0]?e.append("course_map",JSON.stringify(a.state.newCourse.course_map)):e.append(t[0],t[1])}),e},a.handleBackClick=function(){a.setState(function(e){return{step:e.step-1}})},a.handleFieldChange=function(e,t){["course_session","course_number"].includes(e)&&(t=t.replace(/ /g,"").replace(/[^a-zA-Z0-9]/g,"").toLowerCase()),a.setState(function(a){var n;return{newCourse:Object(o.a)({},a.newCourse,(n={},Object(ee.a)(n,e,t),Object(ee.a)(n,"validCourseId",!0),n))}})},a.toggleDialog=function(){a.setState(function(e){return{cancelCreationPopup:!e.cancelCreationPopup}})},a.eraseNewCourse=function(){a.setState({newCourse:Xe,step:0,cancelCreationPopup:!1,selectedCourse:void 0,mode:void 0})},a.getContext=function(){return Object(o.a)({},a.state,{handleFieldChange:a.handleFieldChange,handleNextClick:a.handleNextClick,addCourseDetails:a.addCourseDetails,toggleDialog:a.toggleDialog,handleBackClick:a.handleBackClick,launchCourseCreation:a.launchCourseCreation,checkCourseId:a.checkCourseId,eraseNewCourse:a.eraseNewCourse})},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"componentWillMount",value:function(){var e=this.props.match.params.referredCourseId;if(e){var t=this.state.courses.find(function(t){return t.course_id===e});this.setCourse(t),this.setState({mode:"re-run",step:1})}}},{key:"render",value:function(){var e=this.props.classes,t=this.state,a=t.step,l=t.mode,s=t.selectedCourse,o=t.translations,c=this.state.courses.filter(function(e){return"phileas"===e.type});return r.a.createElement(n.Fragment,null,r.a.createElement(g,{value:this.getContext()},r.a.createElement(_,null),r.a.createElement("div",{className:e.createPageWrapper},0===a&&r.a.createElement(te,{setMode:this.setMode}),1===a&&"re-run"===l&&!s&&r.a.createElement(ne,{courses:c,setCourse:this.setCourse}),[1,2,3,4,5,6].includes(a)&&("new-course"===l||s)&&r.a.createElement(Ve,null)),r.a.createElement(Ze,{openDialog:this.state.cancelCreationPopup,toggleDialog:this.toggleDialog,dialogTitle:o.cancelCreationTitle,dialogContent:o.cancelCreationContent,dialogValid:o.validCancelCreation,dialogCancel:o.backToCourse,dialogAction:this.eraseNewCourse})))}}]),t}(n.Component),et=Object(p.a)(x)(Ye),tt=a(252),at=a(253),nt=a(120),rt=a(53),lt=Object(nt.a)({palette:{primary:{main:"#009FE5"},secondary:{main:"#009FE5"}},overrides:{MuiButton:{text:{fontSize:"0.9rem",border:"none",borderRadius:25,padding:"8px 25px",cursor:"pointer",backgroundColor:"#009FE5",fontWeight:"bold",textTransform:"initial",color:"white!important"}}}});var st=function(){return r.a.createElement("div",null,r.a.createElement(tt.a,null),r.a.createElement(at.a,{theme:lt},r.a.createElement(j.a,{basename:"/"},r.a.createElement(rt.a,{exact:!0,path:"/",component:function(){return r.a.createElement(Q,null)}}),r.a.createElement(rt.a,{path:"/create/:referredCourseId?",component:function(e){return r.a.createElement(et,e)}}))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));s.a.render(r.a.createElement(st,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[139,1,2]]]);
//# sourceMappingURL=main.cef2b583.chunk.js.map