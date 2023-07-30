$(document).ready(function(){
    //****On Load **/
    $.getJSON("http://localhost:8000/api/displayvehicleforuser",{param:'all'},function(data){
        var htm = `<div class="UserVehicleList-rightbartemplate">
                <img src="/static/Subscription.png" width="90%" style="display: flex; margin-left: 7%; margin-top: 2%;">
        </div>`
        data.map((item)=>{
            htm += `<a href='http://localhost:8000/api/displayselectedvehicle/?vehicle=${JSON.stringify(item)}' style="text-decoration: none; cursor: pointer; color: #000;">
            <div class="UserVehicleList-rightbartemplate">
            <img src="/${item.icon}" width="55%" style="display: flex; margin-left: 20%; margin-top: 4%;">
            <div style="margin-left: 8%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 1%;">
            ${item.company_name}
            </div>
            <div style="margin-left: 8%; font-family: Poppins; font-size: 16; font-weight: 600;">
            ${item.subcategory_name}
            </div>
            <div style="margin-left: 5%; font-family: Poppins; font-size: 10; font-weight: 600;">
                <img src="/static/iconDiesel.svg" width="4%"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.fuel_type}</span>
                <img src="/static/iconTransmission.svg" width="11%" style="padding-left: 6%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.transmission_type}</span>
                <img src="/static/iconSeat.svg" width="10%" style="padding-left: 5%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.no_of_seats} Seats</span>
            </div>
            <div style="margin-left: 8%;">
                <div style="font-size: 26px; margin-top: 4%; display: flex; justify-content: space-between;">
                    <div style="display: flex; margin-left: 1%; margin-top: 1%; ">
                        &#8377<span style="font-family: Poppins; font-size: 26px; font-weight: 700;">
                        ${item.price}
                        </span>
                    </div>
                    <div class="UserVehicleList-button_style" style="display: flex; margin-right: 7%; margin-top: 1%;">
                        <div style="display: flex; align-items: center; font-size: 15; color: #fff; font-weight: bold;">Book  ></div>
                    </div>
                </div>
            </div>
            <div style="margin-left: 9%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 5%;">
                288 kms | Price <b>exclude</b> fuel cost 
            </div></a>
        </div>`
        });
        $('#listvehicle').html(htm)
    });
/*****/

    function searching(value){
        $.getJSON("http://localhost:8000/api/displayvehicleforuser",{param:value},function(data){
        var htm = `<div class="UserVehicleList-rightbartemplate">
                <img src="/static/Subscription.png" width="90%" style="display: flex; margin-left: 7%; margin-top: 5%;">
        </div>`
        data.map((item)=>{
            htm += `<a href='http://localhost:8000/api/displayselectedvehicle/?vehicle=${JSON.stringify(item)}' style="text-decoration: none; cursor: pointer; color: #000;">
            <div class="UserVehicleList-rightbartemplate" style="margin-left: 3%;">
            <img src="/${item.icon}" width="55%" style="display: flex; margin-left: 20%; margin-top: 4%;">
            <div style="margin-left: 8%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 1%;">
            ${item.company_name}
            </div>
            <div style="margin-left: 8%; font-family: Poppins; font-size: 16; font-weight: 600;">
            ${item.subcategory_name}
            </div>
            <div style="margin-left: 5%; font-family: Poppins; font-size: 10; font-weight: 600;">
                <img src="/static/iconDiesel.svg" width="4%"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.fuel_type}</span>
                <img src="/static/iconTransmission.svg" width="11%" style="padding-left: 6%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.transmission_type}</span>
                <img src="/static/iconSeat.svg" width="10%" style="padding-left: 5%;"><span style="padding-left: 2%; font-family: Poppins; font-size: 12; font-weight: 500;">${item.no_of_seats} Seats</span>
            </div>
            <div style="margin-left: 8%;">
                <div style="font-size: 26px; margin-top: 4%; display: flex; justify-content: space-between;">
                    <div style="display: flex; margin-left: 1%; margin-top: 1%; ">
                        &#8377<span style="font-family: Poppins; font-size: 26px; font-weight: 700;">
                        ${item.price}
                        </span>
                    </div>
                    <div class="UserVehicleList-button_style" style="display: flex; margin-right: 7%; margin-top: 1%;">
                        <div style="display: flex; align-items: center; font-size: 15; color: #fff; font-weight: bold;">Book  ></div>
                    </div>
                </div>
            </div>
            <div style="margin-left: 5%; font-family: Poppins; font-size: 12; font-weight: 500; margin-top: 5%;">
                288 kms | Price <b>exclude</b> fuel cost 
            </div></a>
        </div>`
        });
        $('#listvehicle').html(htm)
    });
    }
    // $('.brand').click(function(){
    //     var sb = ''
    //     $('.brand').map(function(i,item){
    //         if($(this).prop('checked')){
    //             sb+="'"+$(this).val()+"',"
    //         }
    //     });
    //     sb = sb.substring(0,sb.length-1)
    //     if (sb == '')
    //         searching('all')
    //     else 
    //         searching(sb)
    // })
    // $('.fuel').click(function(){
    //     sft = ''
    //     $('.fuel').map(function(i,item){
    //         if($(this).prop('checked')){
    //             sft+="'"+$(this).val()+"',"
    //         }
    //     });
    //     sft = sft.substring(0,sft.length-1)
    //     if (sft == '')
    //         searching('all')
    //     else 
    //         searching(sft)
    // })
    // $('.transmission').click(function(){
    //     stt = ''
    //     $('.transmission').map(function(i,item){
    //         if($(this).prop('checked')){
    //             stt+="'"+$(this).val()+"',"
    //         }
    //     });
    //     stt = stt.substring(0,stt.length-1)
    //     if (stt == '')
    //         searching('all')
    //     else 
    //         searching(stt)
    // })
    
//    $('.searching').ready(function(){
//     var Q=[]
//     $('.brand').click(function(){
//             var sb = ''
//             $('.brand').map(function(i,item){
//                 if($(this).prop('checked')){
//                     sb+="'"+$(this).val()+"',"
//                     Q = Q.push(sb)
//                 }
//                 alert(Q)
//             });
//             sb = sb.substring(0,sb.length-1)
//            Q = Q.push(sb)
//            alert(Q)
//         })
//    })
var p=[]
let sb=''
let sf=''
$('.brand').click(function(){
    sb=''

    $('.brand').map(function(i,item){
      if($(this).prop("checked")) 
         {sb+="'"+($(this).val())+"' ,"}
        p.push($(this).val())
      //console.log(sb)
      });
      
      sb=sb.substring(0,sb.length-1)
      sb = sb+sf
    //  console.log(p)
      console.log(sb)
    // p.push(sb)
    // if(sb=='')
    //     searching('all')
    // else
    //     searching(sb)
    if(sb=='')
        searching('all')
    else
        searching(sb)

})
$('.fuel').click(function(){
    sf=''
    $('.fuel').map(function(i,item){
      if($(this).prop("checked")) 
      {sf+="'"+($(this).val())+"' ,"}
    });
    sf=sf.substring(0,sf.length-1)
    sb+=sf
    console.log(sb)
    p.push(sf)
    if(sb=='')
        searching('all')
    else
        searching(sb)
    
})
})