(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{136:function(e,t,a){"use strict";a.r(t);var n=a(0),i=a.n(n),c=a(10),l=a.n(c),o=a(73),s=a(74),r=a(87),d=a(75),u=a(17),m=a(88),h=a(182),p=a(29),g=(a(97),a(196)),f=a(180),b=a(77),v=a.n(b);var E=function(e){var t=e.topics,a=(t=t.slice(0,4)).map(function(e,t){return i.a.createElement(f.a,{key:e.nameTopic+t,label:e.nameTopic,value:t})});return i.a.createElement("div",{id:"tabsWrapper"},i.a.createElement(g.a,{id:"tabsElementWrapper",value:e.selectedTopic,indicatorColor:"primary",onChange:e.handleChangeTabTopic,variant:"fullWidth"},a),e.topics.length<4&&i.a.createElement(h.a,{id:"addTopicButton",color:"primary",size:"small",variant:"contained",onClick:function(t){e.addField("topic",t)}}," ",i.a.createElement(v.a,null)," "))},T=a(194),C=a(199);var S=function(e){return i.a.createElement("div",{className:"langPicker",style:{textAlign:"right",padding:" 10px 0px"}},i.a.createElement(T.a,{value:e.lang,onChange:e.selectLang},i.a.createElement(C.a,{value:"fr"},"Fr"),i.a.createElement(C.a,{value:"en"},"En")))},y=a(30),k=a(86),F=(a(106),a(85)),j=a(197),N=a(139),O=a(201),I=a(81),w=a.n(I),D=a(82),q=a.n(D),x=a(80),J=a.n(x),A=a(184),z=a(185),W=a(186),L=a(200),_=a(187),Q=a(188),R=a(189),B=a(58),P=a.n(B),V=a(195);a(127),a(128),a(129),a(131),a(133),a(72);function M(e){var t=i.a.useState(!1),a=Object(k.a)(t,2),n=a[0],c=a[1],l=e.topics;l=l.slice(0,4);var o=function(){c(!1)},s=function(){c(!0)},r=l.map(function(t,a){var n;return i.a.createElement("div",{className:"tabTopic",key:t+a},i.a.createElement(A.a,{className:"topicInput"},i.a.createElement(z.a,null,i.a.createElement("center",null,i.a.createElement("h4",null,t.nameTopic))),i.a.createElement(W.a,null,i.a.createElement("div",{className:"TopicName"},i.a.createElement("div",{className:"inputTopicWrapper"},i.a.createElement(V.a,{className:"inputTopic",label:"Nom",onChange:function(t){e.handleChange(t.target.value,[a,"topic","name"])},value:t.nameTopic}),i.a.createElement(V.a,{className:"inputTopic",label:"ic\xf4ne",onChange:function(t){e.handleChange(t.target.value,[a,"topic","icon"])},value:t.icon,InputProps:{endAdornment:i.a.createElement(O.a,{position:"end"},i.a.createElement(N.a,{edge:"end","aria-label":"Toggle Image",onClick:s},i.a.createElement(w.a,{size:"small"})))}})),i.a.createElement("div",null,i.a.createElement(h.a,{className:"buttonStylised",color:"primary",style:{color:"#fff"},variant:"contained",onClick:function(t){e.addField("subTopic",a)},size:"small"},"Ajouter un sous-topic "),i.a.createElement(h.a,{className:"buttonStylised",color:"secondary",style:{color:"#fff"},variant:"contained",onClick:function(t){e.removeField("topic",a)},size:"small"},"Supprimer"))))),i.a.createElement("div",{className:"topicContent"},i.a.cloneElement(e.children,{topics:l[a],idx:a})),i.a.createElement("div",{className:"buttonWrapper"},i.a.createElement(h.a,{className:"submitJson buttonStylised",style:{color:"#fff"},color:"primary",size:"small",variant:"contained",onClick:function(t){e.handleSubmit(t)}}," Valider "),!0===e.change&&i.a.createElement("div",{id:"cancel"},i.a.createElement("p",{className:"buttonStylised warningChange"},"Des Changements sont en cours"),i.a.createElement(h.a,(n={className:"buttonStylised"},Object(y.a)(n,"className","reinitJson"),Object(y.a)(n,"style",{color:"#fff"}),Object(y.a)(n,"color","secondary"),Object(y.a)(n,"size","small"),Object(y.a)(n,"variant","contained"),Object(y.a)(n,"onClick",function(t){e.handleCancel(t)}),n)," Annuler "))))});return i.a.createElement(J.a,{axis:"x",index:e.selectedTopic,onChangeIndex:e.handleChangeTabTopic},r,i.a.createElement(j.a,{open:n,onClose:o,style:{textAlign:"center",display:"grid"}},i.a.createElement("div",null,i.a.createElement("span",{style:{height:"100%",verticalAlign:"middle",display:"inline-block"}}),i.a.createElement("img",{className:"previewImg",src:e.topics[e.selectedTopic].icon,alt:e.topics[e.selectedTopic].icon}),i.a.createElement(N.a,{style:{position:"absolute",backgroundColor:"#ff6d00"},edge:"end","aria-label":"Close Image",onClick:o,color:"secondary"},i.a.createElement(q.a,{style:{color:"white"},size:"small"})))))}function U(e){var t=e.topics.content.map(function(t,a){return i.a.createElement(L.a,{key:a},i.a.createElement(_.a,{className:"sousTopic",expandIcon:i.a.createElement(P.a,null),"aria-controls":"panel1bh-content",id:"panel1bh-header"},i.a.createElement("h3",null,t.nameSubTopic)),i.a.createElement(Q.a,{className:"subTopicFields"},i.a.createElement(V.a,{label:"Nom du sous-topic",onChange:function(t){e.handleChange(t.target.value,[e.idx,"subtopic",a])},fullWidth:!0,rows:"12",value:t.nameSubTopic}),i.a.cloneElement(e.children,{data:t.content,topic:e.idx,subTopic:a})),i.a.createElement(R.a,null,i.a.createElement(h.a,{color:"primary",onClick:function(t){e.addField("question",e.idx,a)},size:"small"},"Ajouter une question "),i.a.createElement(h.a,{color:"secondary",onClick:function(t){e.removeField("subTopic",e.idx,a)},size:"small"},"Supprimer")))});return i.a.createElement("div",null,t)}function G(e){var t=e.data.map(function(t,a){return i.a.createElement(L.a,{key:a},i.a.createElement(_.a,{expandIcon:i.a.createElement(P.a,null),"aria-controls":"panel1bh-content",id:"panel1bh-header"},i.a.createElement("h4",null,t.question)),i.a.createElement(Q.a,{className:"qAndAFields"},i.a.createElement(V.a,{label:"Question",fullWidth:!0,rows:"12",value:t.question,onChange:function(t){e.handleChange(t.target.value,[e.topic,e.subTopic,"question",a])}}),i.a.createElement("p",null,"R\xe9ponse:"),i.a.createElement(F.a,{inline:!0,className:"tiny",init:{language_url:window.tineMceFR,language:"fr_FR",plugins:"link image code"},initialValue:t.response,onChange:function(t){e.handleChange(t.level.content,[e.topic,e.subTopic,"response",a])}})),i.a.createElement(R.a,null,i.a.createElement(h.a,{color:"secondary",onClick:function(t){e.removeField("question",e.topic,e.subTopic,a)},size:"small"},"Supprimer")))});return i.a.createElement("div",{className:"qAndAWrappers"},t)}var X=a(190),H=function(e){function t(e){var a;return Object(o.a)(this,t),(a=Object(r.a)(this,Object(d.a)(t).call(this,e))).handleChangeSubtopic=function(e){return function(e,t){return!!t}},a.state={lang:"fr",selectedTopic:0,expanded:!1,data:[],dataOld:[],change:!1,loading:!0},a.handleChangeTabTopic=a.handleChangeTabTopic.bind(Object(u.a)(a)),a.handleChangeSubtopic=a.handleChangeSubtopic.bind(Object(u.a)(a)),a.handleChange=a.handleChange.bind(Object(u.a)(a)),a.handleSubmit=a.handleSubmit.bind(Object(u.a)(a)),a.handleCancel=a.handleCancel.bind(Object(u.a)(a)),a.addField=a.addField.bind(Object(u.a)(a)),a.removeField=a.removeField.bind(Object(u.a)(a)),a.initData=a.initData.bind(Object(u.a)(a)),a.fetchingData=a.fetchingData.bind(Object(u.a)(a)),a.postingData=a.postingData.bind(Object(u.a)(a)),a.selectLang=a.selectLang.bind(Object(u.a)(a)),a}return Object(m.a)(t,e),Object(s.a)(t,[{key:"fetchingData",value:function(){var e=this;fetch("/tma_cms_apps/api/v1/microsite_manager/json/"+window.siteID.siteID+"/faq/",{credentials:"same-origin",method:"GET"}).then(function(e){return e.json()}).then(function(t){var a=t;e.setState({data:p.a.fromJS(a),loading:!1,dataOld:p.a.fromJS(a)})})}},{key:"postingData",value:function(){var e=this;fetch("/tma_cms_apps/api/v1/microsite_manager/json/"+window.siteID.siteID+"/faq/",{credentials:"same-origin",method:"PUT",body:JSON.stringify(this.state.data.toJS()),headers:{Accept:"application/json","Content-Type":"application/json","X-CSRFToken":window.csrf}}).then(function(e){return e.json()}).then(function(t){e.fetchingData()})}},{key:"selectLang",value:function(e){this.setState({lang:e.target.value})}},{key:"handleChangeTabTopic",value:function(e,t){this.setState({selectedTopic:t})}},{key:"addField",value:function(e,t,a){var n=this;"topic"===e&&this.setState(function(e){return{data:e.data.updateIn([n.state.lang],function(e){return e.push(p.a.fromJS({content:[],icon:"",idTopic:"",nameTopic:"TopicName"}))})}}),"subTopic"===e&&this.setState(function(e){return{data:e.data.updateIn([n.state.lang,t,"content"],function(e){return e.push(p.a.fromJS({nameSubTopic:"SubTopicName",content:[]}))})}}),"question"===e&&this.setState(function(e){return{data:e.data.updateIn([n.state.lang,t,"content",a,"content"],function(e){return e.push(p.a.fromJS({namequestion:"Question",question:"Question",response:""}))})}})}},{key:"removeField",value:function(e,t,a,n){var i=this;"topic"===e&&(this.state.selectedTopic>this.state.data.toJS()[this.state.lang].length-2?this.setState(function(e){var a=e.data;return{selectedTopic:t>0?t-1:0,data:a.deleteIn([i.state.lang,t])}}):this.setState(function(e){return{data:e.data.deleteIn([i.state.lang,t])}})),"subTopic"===e&&this.setState(function(e){return{data:e.data.deleteIn([i.state.lang,t,"content",a])}}),"question"===e&&this.setState(function(e){return{data:e.data.deleteIn([i.state.lang,t,"content",a,"content",n])}})}},{key:"handleChange",value:function(e,t){var a=this;"topic"===t[1]?"name"===t[2]?this.setState(function(n){return{data:n.data.updateIn([a.state.lang,t[0],"nameTopic"],function(t){return e})}}):"icon"===t[2]&&this.setState(function(n){return{data:n.data.updateIn([a.state.lang,t[0],"icon"],function(t){return e})}}):"subtopic"===t[1]?this.setState(function(n){return{data:n.data.updateIn([a.state.lang,t[0],"content",t[2],"nameSubTopic"],function(t){return e})}}):"question"===t[2]?this.setState(function(n){return{data:n.data.updateIn([a.state.lang,t[0],"content",t[1],"content",t[3],"question"],function(t){return e})}}):"response"===t[2]&&this.setState(function(n){return{data:n.data.updateIn([a.state.lang,t[0],"content",t[1],"content",t[3],"response"],function(t){return e})}})}},{key:"detecteChange",value:function(e){this.setState({change:e})}},{key:"handleSubmit",value:function(e){this.postingData()}},{key:"handleCancel",value:function(){this.fetchingData()}},{key:"componentWillMount",value:function(){0===this.state.data.length?this.fetchingData():alert("Ereur lors de la r\xe9cup\xe9ration des donn\xe9es, veuillez contacter un administrateur !")}},{key:"componentDidUpdate",value:function(){this.state.data.equals(this.state.dataOld)?this.state.change&&this.detecteChange(!1):this.state.change||this.detecteChange(!0)}},{key:"initData",value:function(){var e=this;this.setState(function(t){return{data:t.data.updateIn([e.state.lang],function(e){return e.push(p.a.fromJS({content:[],icon:"",idTopic:"",nameTopic:"TopicName"}))})}})}},{key:"render",value:function(){var e=this;return i.a.createElement("div",{className:"wrapperFAQ"},this.state.loading?i.a.createElement("center",null,i.a.createElement(X.a,null)):0===this.state.data.toJS()[this.state.lang].length?i.a.createElement("div",null,i.a.createElement(S,{selectLang:this.selectLang,lang:this.state.lang}),i.a.createElement("div",{className:"noTopic"}," Vous n'avez aucun topic ",i.a.createElement(h.a,{id:"initTopicButton",color:"primary",variant:"contained",onClick:function(){e.initData()}},"Cr\xe9er un topic"))):i.a.createElement("div",{id:"mainWrapper"},i.a.createElement(S,{selectLang:this.selectLang,lang:this.state.lang}),i.a.createElement(E,{topics:this.state.data.toJS()[this.state.lang],selectedTopic:this.state.selectedTopic,handleChangeTabTopic:this.handleChangeTabTopic,addField:this.addField}),i.a.createElement(M,{change:this.state.change,handleSubmit:this.handleSubmit,handleCancel:this.handleCancel,topics:this.state.data.toJS()[this.state.lang],selectedTopic:this.state.selectedTopic,removeField:this.removeField,handleChangeTabTopic:this.handleChangeTabTopic,handleChange:this.handleChange,addField:this.addField},i.a.createElement(U,{handleChange:this.handleChange,selectedTopic:this.state.selectedTopic,addField:this.addField,removeField:this.removeField},i.a.createElement(G,{handleChange:this.handleChange,addField:this.addField,removeField:this.removeField})))))}}]),t}(i.a.Component),K=a(198),Y=a(84),Z=a(192),$=a(191),ee=Object(Y.a)({palette:{primary:{main:"#5cb7d8"},secondary:$.a},background:"#5cb7d8"});l.a.render(i.a.createElement(Z.a,{theme:ee},i.a.createElement(K.a,null),i.a.createElement(H,null)),document.getElementById("root"))},92:function(e,t,a){e.exports=a(136)},97:function(e,t,a){}},[[92,1,2]]]);
//# sourceMappingURL=main.3062330a.chunk.js.map