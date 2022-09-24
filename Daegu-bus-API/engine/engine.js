const client = require('cheerio-httpcli')
const iconv = require('iconv-lite')
const dateformat = require('dateformat')
const { cp } = require('fs')

module.exports = {
  route : {
    search: (searchtext, callback) => {
      let str = ''
      const buf = iconv.encode(searchtext, 'EUC-KR')
      for (let i = 0; i < buf.length; i++) {
        str += '%' + buf[i].toString(16).toUpperCase()
      }
      const url = "http://businfo.daegu.go.kr/ba/route/route.do?act=findByNo&routeNo=" + str + "&nsbus=false"

      const call = (err, $, res, body) => {
        if (err) {
          console.log(err)
          return
        }

        const result = []
        let lastbus = ''
        $("td.body_col2").each(function(idx) {
          const onclick = $(this).attr("onclick")
          const text = $(this).text().trim()
          const id = onclick.slice(onclick.indexOf("'") + 1, onclick.lastIndexOf("'"))
          if (id.substr(0,4)=="node"){
            lastbus = text
          }
          else if (text.substr(0, 1) == '-') {
              result.push({
                이름 : lastbus,
                방면 : text.substr(2),
                버스id : id
              })
          } else {
            result.push({
              이름 : text,
              방면 : "없음",
              버스id : id
            })
          }
        })

        callback(result)
      }

      client.fetch(url, 'EUC-KR', call)
    },
    route : (id, callback) => {
     const date = new Date()
     const url = "http://businfo.daegu.go.kr/ba/route/rtbspos.do?act=findByPos&routeId="+id+"&svcDt="+dateformat(date,'yyyymmdd')

     const call = (err, $, res, body) => {
       if (err) {
         console.log(err)
         return
       }

       const result = {
         버스번호 : {
          이름:[]
        },
         정방향 : {
           노선:[],
           현재:[]
         },
         역방향 : {
           노선:[],
           현재:[]
         }
       }
       
         const selectorcall = function(idx) {
         let text = $(this).text().trim()
         console.log(text)    
         if (text.length != 0){
           if (text.substr(-7)[0]=='('){ //station
             text = text.substr(0,text.length-7).trim()
             is정방향.노선.push(text)
             lasttext = text
             console.log('station : '+text)
           }
           else if (text.substr(-10)[0]=='('){ //bus
             text = text.substr(0,text.length-10).trim()
             if (text.length != 0){
               is정방향.현재.push(lasttext+' '+text)
               console.log('bus : '+lasttext)
               console.log('bus : '+text)
             }
           }
          }
       }

       $("#posResultRed3").each(function(idx){
        text = $(this).text().trim()
        if (text.length != 0){
          result.버스번호.이름.push(text);
        }
      })
       let is정방향= result.정방향
       let lasttext = "start"
       $("#posForwardPanel tr>*").each(selectorcall)
       is정방향 = result.역방향
       lasttext = "start"
       $("#posBackwardPanel tr>*").each(selectorcall)

       callback(result)
     }

     client.fetch(url, 'EUC-KR', call)
   }
  },
  station : {
    search: (searchtext, callback) => {
      let str = ''
      const buf = iconv.encode(searchtext, 'EUC-KR')
      for (let i = 0; i < buf.length; i++) {
        str += '%' + buf[i].toString(16).toUpperCase()
      }
      const url = "http://businfo.daegu.go.kr/ba/route/rtbsarr.do?act=findByBS2&bsNm="+str

      const call = (err, $, res, body) => {
        if (err) {
          console.log(err)
          return
        }

        const result = []
        let lastbus = ''
        $("#arrResultBsPanel td.body_col1").each(function(idx) {
          const onclick = $(this).attr("onclick")
          const firstcom = onclick.indexOf("'")
          const lastcom = onclick.indexOf("'",firstcom+1)
          const id = onclick.substr(firstcom+1,lastcom-firstcom-1)
          let text = $(this).text().trim()
          text = text.substr(0,text.length-7).trim()
          result.push({
            이름 : text,
            정류장id : id
          })

        })

        callback(result)
      }

      client.fetch(url, 'EUC-KR', call)
    },
    station: (id, callback) => {
      let routelength
      const result = []
      const buscallback=(data)=>{
        result.push(data)
        if (result.length==routelength){
          callback(result)
        }
      }
      const routecall=(data)=>{
        routelength = data.length
        for (let i = 0; i < data.length; i++) {
          module.exports.station.bus(data[i],buscallback)
        }
      }
      module.exports.station.routes(id,routecall)
    },
    stationrow: (id, callback) => {
      let routelength
      const result = []
      const rowbuscallback=(data)=>{
        result.push(data)
        if (result.length==routelength){
          callback(result)
        }
      }
      const routecall=(data)=>{
        routelength = data.length
        for (let i = 0; i < data.length; i++) {
          module.exports.station.rowbus(data[i],rowbuscallback)
        }
      }
      module.exports.station.routes(id,routecall)
    },
    routes: (id, callback) => {
      const url = "http://businfo.daegu.go.kr/ba/route/rtbsarr.do?act=findByPath&x=&y=&bsId="+id

      const call = (err, $, res, body) => {
        if (err) {
          console.log(err)
          return
        }

        const result = []
        let lastbus = ''
        $("td.body_col2").each(function(idx) {
          const onclick = $(this).attr("onclick")
          const quo = []
          quo[0] = onclick.indexOf("'")
          for (var i = 1; i <= 9; i++) {
            quo[i] = onclick.indexOf("'",quo[i-1]+1)
          }
          const pick = (i=>onclick.substr(quo[2*i]+1,quo[2*i+1]-quo[2*i]-1))
          const stationid = pick(0)
          const routeid = pick(2)
          const forward = pick(4)
          let text = $(this).text().trim()
          if (stationid.substr(0,4)=="node"){
            lastbus = text
          }
          else if (text.substr(0, 1) == '-') {
              result.push({
                이름 : lastbus,
                방면: text.substr(2),
                정류장id : stationid,
                버스id : routeid,
                방향 : forward
              })
          } else {
            result.push({
              이름 : text,
              방면 : "없음",
              정류장id : stationid,
              버스id : routeid,
              방향 : forward
            })
          }
        })

        callback(result)
      }

      client.fetch(url, 'EUC-KR', call)
    },
    bus: (data, callback) => {
      const stationid = data.정류장id
      const routeid = data.버스id
      const forward = data.방향
      const url = "http://businfo.daegu.go.kr/ba/route/rtbsarr.do?act=findByArr&bsNm=&routeNo=&winc_id=02283&bsId="+stationid+"&routeId="+routeid+"&moveDir="+forward
      const call = (err, $, res, body) => {
        if (err) {
          console.log(err)
          return
        }

        const buslist=[]
        const result = {
          이름: data.이름,
          방면: data.방면,
          버스id: data.버스id,
          방향: data.방향}
        //station, interval, wait
        $("table").each(function(){
          const col3 = []
          const col4 = []
          const res = {}
          $(this).find('td.body_col3').each(function(){
            col3.push($(this).text())
          })
          $(this).find('td.body_col4').each(function(){
            col4.push($(this).text())
          })
          for (let i = 0; i < col3.length; i++) {
              res[col3[i]]=col4[i]
            }
          if (Object.keys(res).length!=0)
          {buslist.push(res)}
        })

        result.버스 = buslist
        callback(result)
      }

      client.fetch(url, 'EUC-KR', call)
      
    },
    rowbus:(data, callback) =>{
      const stationid = data.정류장id
      const routeid = data.버스id
      const forward = data.방향
      const url = "http://businfo.daegu.go.kr/ba/route/rtbsarr.do?act=findByArr&bsNm=&routeNo=&winc_id=02283&bsId="+stationid+"&routeId="+routeid+"&moveDir="+forward
      const call = (err, $, res, body) => {
        if (err) {
          console.log(err)
          return
        }

        const buslist=[]
        const result = {}
        //station, interval, wait
        $("table").each(function(){
          const col3 = []
          const col4 = []
          const res = {}

          $(this).find('td.body_col3').each(function(){
            col3.push($(this).text())
          })
          $(this).find('td.body_col4').each(function(){
            col4.push($(this).text())
          })
           for (let i = 0; i < col3.length; i++) {
            res[col3[i]]=col4[i]
            }
          if (Object.keys(res).length!=0 && res.버스번호.includes('(')){
              {buslist.push(res)}
              result.이름 = data.이름,
              result.방면= data.방면,
              result.버스id= data.버스id,
              result.방향= data.방향
          }
        })

        result.버스 = buslist
        callback(result)
      }

      client.fetch(url, 'EUC-KR', call)
      
    },   
  }
}