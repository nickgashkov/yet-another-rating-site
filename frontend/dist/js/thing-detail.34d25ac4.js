(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["thing-detail"],{1935:function(t,e,n){"use strict";n.r(e);var i=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("thing-detail-container")},a=[],l=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("app-detail",{attrs:{item:t.thing}})},o=[],s=n("2f62"),p=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("span",[t._v(t._s(t.item.name))])},r=[],u={name:"AppDetail",props:{item:Object}},c=u,h=n("2877"),m=Object(h["a"])(c,p,r,!1,null,null,null);m.options.__file="AppDetail.vue";var _=m.exports,d=Object(s["a"])("things"),f=d.mapState,g=d.mapActions,v={name:"ThingDetailContainer",components:{AppDetail:_},mounted:function(){this.loadThing({id:this.$route.params.id})},computed:f(["thing"]),methods:g(["loadThing"])},D=v,b=Object(h["a"])(D,l,o,!1,null,null,null);b.options.__file="ThingDetailContainer.vue";var T=b.exports,w={name:"ThingDetail",components:{ThingDetailContainer:T}},j=w,O=Object(h["a"])(j,i,a,!1,null,null,null);O.options.__file="ThingDetail.vue";e["default"]=O.exports}}]);
//# sourceMappingURL=thing-detail.34d25ac4.js.map