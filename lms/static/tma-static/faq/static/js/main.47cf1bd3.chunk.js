(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{10:function(e,t,a){"use strict";a.r(t);var n=a(2),s=a(3),c=a(5),i=a(4),o=a(1),r=a(6),l=a(0),h=a.n(l),u=a(8),m=a.n(u),p=(a(16),a(17),function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(c.a)(this,Object(i.a)(t).call(this,e))).handleClick=a.handleClick.bind(Object(o.a)(a)),a.handleSearch=a.handleSearch.bind(Object(o.a)(a)),a.handleLanguage=a.handleLanguage.bind(Object(o.a)(a)),a.state={topicOnScreen:a.props.data[window.lang].nameTopic,language:window.lang,search:""},a}return Object(r.a)(t,e),Object(s.a)(t,[{key:"handleClick",value:function(e){this.setState({topicOnScreen:e}),this.setState({search:""})}},{key:"handleSearch",value:function(e){this.setState({search:e})}},{key:"handleLanguage",value:function(e){this.setState({language:e})}},{key:"render",value:function(){var e=this.props.data[this.state.language],t=[],a=[];console.log(e),4<e.length?(t=e.slice(0,4),a=e.slice(0,4)):(t=e,a=e);var n={};return t.forEach(function(e,t){n[e.nameTopic]=t}),""===this.state.search&&(t=t[n[this.state.topicOnScreen]]?t[n[this.state.topicOnScreen]]:t[0]),console.log(a),h.a.createElement("div",{className:"main"},h.a.createElement("div",{className:"contentWrapper"},h.a.createElement(d,{data:a,onScreen:this.state.topicOnScreen,handleChangeState:this.handleClick,searchKeyword:this.state.search,handleSearchBar:this.handleSearch}),h.a.createElement(g,{data:t,searchKeyword:this.state.search})))}}]),t}(h.a.Component)),d=function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(c.a)(this,Object(i.a)(t).call(this,e))).handleInputSearch=a.handleInputSearch.bind(Object(o.a)(a)),a}return Object(r.a)(t,e),Object(s.a)(t,[{key:"handleInputSearch",value:function(e){this.props.handleSearchBar(e.target.value)}},{key:"handleSelectedTopic",value:function(e){if("LI"===e.target.tagName){for(var t=0;t<e.target.parentNode.children.length;t++)e.target.parentNode.children[t].children[0].classList.remove("selected");e.target.children[0].classList.add("selected")}else{for(var a=0;a<e.target.parentNode.parentNode.children.length;a++)e.target.parentNode.parentNode.children[a].children[0].classList.remove("selected");e.target.parentNode.children[0].classList.add("selected")}!function(){for(var e=0;e<document.getElementsByClassName("question").length;e++){document.getElementsByClassName("question")[e].nextSibling.style.maxHeight="0px"}}()}},{key:"componentDidMount",value:function(){}},{key:"render",value:function(){var e=this,t=this.props.data,a=[];return console.log(t),t.forEach(function(n){console.log(n),t[0].nameTopic===n.nameTopic?a.push(h.a.createElement("li",{key:n.nameTopic,className:"topic",onClick:function(t){e.props.handleChangeState(n.nameTopic),e.handleSelectedTopic(t)}},h.a.createElement("img",{alt:n.nameTopic,className:"selected",src:n.icon}),h.a.createElement("p",null,n.nameTopic))):a.push(h.a.createElement("li",{key:n.nameTopic,className:"topic",onClick:function(t){e.props.handleChangeState(n.nameTopic),e.handleSelectedTopic(t)}},h.a.createElement("img",{alt:n.nameTopic,src:n.icon}),h.a.createElement("p",null,n.nameTopic)))}),h.a.createElement("div",{className:"search"},h.a.createElement("div",{className:"searchBar"},h.a.createElement("form",null,h.a.createElement("input",{type:"text",placeholder:"Rechercher",value:this.props.searchKeyword,onChange:function(t){e.handleInputSearch(t)}}))),h.a.createElement("ul",{className:"topicMenu"},a))}}]),t}(h.a.Component),g=function(e){function t(){return Object(n.a)(this,t),Object(c.a)(this,Object(i.a)(t).apply(this,arguments))}return Object(r.a)(t,e),Object(s.a)(t,[{key:"render",value:function(){var e=this,t=this.props.data,a=[];return""!==this.props.searchKeyword?t.forEach(function(t,n){t.content.forEach(function(n,s){n.content.forEach(function(n,s){-1!==n.question.toLowerCase().indexOf(e.props.searchKeyword.toLowerCase())?a.push(h.a.createElement("div",{key:t.nameTopic+n.nameQuestion+"_"+s},h.a.createElement(f,{nameTopic:t.nameTopic,data:n,onSearch:!0,searchKeyword:e.props.searchKeyword}))):-1!==n.response.indexOf(e.props.searchKeyword)&&a.push(h.a.createElement("div",null,h.a.createElement(f,{nameTopic:t.nameTopic,data:n,onSearch:!0,searchKeyword:e.props.searchKeyword})))})})}):t.content.forEach(function(e,t){a.push(h.a.createElement(f,{key:t,data:e,onSearch:!1}))}),""!==this.props.searchKeyword?h.a.createElement("div",null,h.a.createElement("h3",null," Recherche de:  ",h.a.createElement("span",{className:"searchKeyWord"},'"',this.props.searchKeyword,'"')," "),h.a.createElement("p",null,a.length+" R\xe9sultats"," "),a):h.a.createElement("div",null,a)}}]),t}(h.a.Component),f=function(e){function t(){return Object(n.a)(this,t),Object(c.a)(this,Object(i.a)(t).apply(this,arguments))}return Object(r.a)(t,e),Object(s.a)(t,[{key:"componentDidMount",value:function(){for(var e=0;e<document.getElementsByClassName("subTopicRow").length;e++)for(var t=0;t<document.getElementsByClassName("subTopicRow")[e].getElementsByClassName("question").length;t++)document.getElementsByClassName("subTopicRow")[e].getElementsByClassName("question")[t].nextSibling.setAttribute("height",document.getElementsByClassName("subTopicRow")[e].getElementsByClassName("question")[t].nextSibling.offsetHeight)}},{key:"render",value:function(){var e,t=this.props.data,a=this.props.onSearch;return e=t.nameSubTopic,a?h.a.createElement("div",{className:"subTopicRow onSearch"},h.a.createElement("h3",{className:"subTopic"},e),h.a.createElement(b,{nameTopic:this.props.nameTopic,data:t,onSearch:a})):h.a.createElement("div",{className:"subTopicRow"},h.a.createElement("h3",{className:"subTopic"},e),h.a.createElement(b,{nameTopic:this.props.nameTopic,data:t,onSearch:a}))}}]),t}(h.a.Component),b=function(e){function t(){return Object(n.a)(this,t),Object(c.a)(this,Object(i.a)(t).apply(this,arguments))}return Object(r.a)(t,e),Object(s.a)(t,[{key:"render",value:function(){var e=[],t=this.props.data,a=this.props.nameTopic;return this.props.onSearch?e.push(h.a.createElement(y,{onSearch:!0,key:a,question:t.question,response:t.response,nameTopic:a})):t.content.forEach(function(t,a){e.push(h.a.createElement(y,{key:a,question:t.question,response:t.response}))}),h.a.createElement("div",{className:"rowQuestionAnswer"},e)}}]),t}(h.a.Component),y=function(e){function t(e){var a;return Object(n.a)(this,t),(a=Object(c.a)(this,Object(i.a)(t).call(this,e))).handleAnimationOnclick=a.handleAnimationOnclick.bind(Object(o.a)(a)),a.handleAnimation=a.handleAnimation.bind(Object(o.a)(a)),a}return Object(r.a)(t,e),Object(s.a)(t,[{key:"handleAnimation",value:function(e,t){var a="";if(""!==(a=t?e.nextSibling:e.target.nextSibling).style.height&&"0px"!==a.style.height||(a.style.height="auto",a.setAttribute("height",a.offsetHeight)),a.offsetHeight>0){a.previousSibling.classList.remove("questionIsClosed"),cancelAnimationFrame(i),cancelAnimationFrame(s);var n=a.offsetHeight,s=function e(){n>=0&&((n-=15)<0&&(n=0),a.style.maxHeight=n+"px",requestAnimationFrame(e))};requestAnimationFrame(s)}else if(a.offsetHeight<=0){a.previousSibling.classList.add("questionIsClosed"),a.style.height="auto";var c=0;cancelAnimationFrame(i),cancelAnimationFrame(s);var i=function e(){c!==a.attributes[2].value&&(c+=15,a.style.maxHeight=c+"px",(c>a.attributes[2].value||c===a.attributes[2].value)&&(a.style.maxHeight=""),requestAnimationFrame(e))};requestAnimationFrame(i)}}},{key:"handleAnimationOnclick",value:function(e){this.handleAnimation(e)}},{key:"componentDidMount",value:function(){if(!this.props.onSearch)for(var e=0;e<document.getElementsByClassName("question").length;e++)document.getElementsByClassName("question")[e].nextSibling.offsetHeight>0&&this.handleAnimation(document.getElementsByClassName("question")[e],!0)}},{key:"componentDidUpdate",value:function(){if(!this.props.onSearch)for(var e=0;e<document.getElementsByClassName("question").length;e++)document.getElementsByClassName("question")[e].nextSibling.offsetHeight>0&&this.handleAnimation(document.getElementsByClassName("question")[e],!0)}},{key:"createMarkup",value:function(e){return{__html:e}}},{key:"render",value:function(){var e=this;return this.props.onSearch?h.a.createElement("div",{className:"questionSection"},h.a.createElement("h5",{className:"question questionIsClosed",onClick:function(t){e.handleAnimationOnclick(t)}},this.props.question," ",h.a.createElement("span",null," ",this.props.nameTopic)),h.a.createElement("p",{className:"response"},h.a.createElement("div",{dangerouslySetInnerHTML:this.createMarkup(this.props.response)}))):h.a.createElement("div",{className:"questionSection"},h.a.createElement("h5",{className:"question questionIsClosed",onClick:function(t){e.handleAnimationOnclick(t)}},this.props.question),h.a.createElement("p",{className:"response"},h.a.createElement("div",{dangerouslySetInnerHTML:this.createMarkup(this.props.response)})))}}]),t}(h.a.Component);m.a.render(h.a.createElement(p,{data:window.props}),document.getElementById("root"))},16:function(e,t,a){},17:function(e,t,a){e.exports=a.p+"static/media/icon.831c46b9.png"},9:function(e,t,a){e.exports=a(10)}},[[9,1,2]]]);
//# sourceMappingURL=main.47cf1bd3.chunk.js.map