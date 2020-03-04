$( document ).ready(function() {
    load_movielist();
    load_mean();
});


function load_movielist(){
    var movieList;
    var html;
    $("#load_movieList").click(function(){  
    
        var url="/restex";  
        //var params="param1="+param1+"¶m2="+param1;  
  
        $.ajax({      
            type:"POST",  
            url:url,      
            //data:params,      
            success:function(args){
                movieList = args;
                for(var i=0;i<args.length;i++){
                    html = "<tr>"
                            + "<td>" + args[i].fixed_acidity + "</td>" 
                            + "<td>" + args[i].volatile_acidity + "</td>"
                            + "<td>" + args[i].citric_acid + "</td>"
                            + "<td>" + args[i].residual_sugar + "</td>"
                            + "<td>" + args[i].chlorides + "</td>"
                            + "<td>" + args[i].free_sulfur_dioxide + "</td>"
                            + "<td>" + args[i].total_sulfur_dioxide + "</td>"
                            + "<td>" + args[i].density + "</td>"
                            + "<td>" + args[i].pH + "</td>"
                            + "<td>" + args[i].sulphates + "</td>"
                            + "<td>" + args[i].alcohol + "</td>"
                            + "<td>" + args[i].quality + "</td>"
                            "</tr>";
                    $("#movieList").append(html);
                }
                
                console.log(args);
            },   
            beforeSend:function(){
                $("#movieList").empty();
                $("#chart").empty();  
            },
            error:function(e){  
                alert(e.responseText);  
            }  
        });  
      
    });
}


function load_mean(){
    var mean_list;
    var html;
    var meanlist = [];
    var keys = [];
    var temp = [];
    $("#load_mean").click(function(){  
    
        var url="/mean";  
        //var params="param1="+param1+"¶m2="+param1;  
  
        $.ajax({      
            type:"POST",  
            url:url,      
            //data:params,      
            success:function(args){
            	mean_list = args;
                keys = Object.keys(args[0]);
                for(var i=0;i<args.length;i++){
                    temp.push(Object.values(args[i]));
                }
                if (temp.length == args.length) {
                  var dataset = Array.from(temp);
                  for (var i = 0; i < 12; i++) {
                    var k = 0;
                    var taeho = [];
                    for (var j = 0; j < dataset.length; j++) {
                      taeho.push(dataset[j][i]);
                    }
                    var mean = d3.mean(taeho);
                    meanlist.push(mean);
                  }}
	              var div = d3
	                .select(".chart")
	                .selectAll("div")
	                .data(meanlist)
	                .enter()
	                .append("div")
	                //.style("width", "0px")
	                .transition()
	                .duration(2000)
	                .style("width", function(d) {
	                  return d * 30 + "px";
	                })
	                .style("height", function(d) {
	                  return 40 + "px";
	                })
	                .text(function(d, i) {
	                  return keys[i] + ">>" + d.toFixed(3);
	                });
                
                html = "<tr>"
                    + "<td>" + Math.round(meanlist[0]*100000)/100000.0 + "</td>" 
                    + "<td>" + Math.round(meanlist[1]*100000)/100000.0 + "</td>"
                    + "<td>" + Math.round(meanlist[2]*100000)/100000.0 + "</td>"
                    + "<td>" + Math.round(meanlist[3]*100000)/100000.0 + "</td>"
                    + "<td>" + Math.round(meanlist[4]*100000)/100000.0 + "</td>"
                    + "<td>" + Math.round(meanlist[5]*100000)/100000.0 + "</td>"
                    + "<td>" + Math.round(meanlist[6]*100000)/100000.0 + "</td>"
                    + "<td>" + Math.round(meanlist[7]*100000)/100000.0 + "</td>"
                    + "<td>" + Math.round(meanlist[8]*100000)/100000.0 + "</td>"
                    + "<td>" + Math.round(meanlist[9]*100000)/100000.0 + "</td>"
                    + "<td>" + Math.round(meanlist[10]*100000)/100000.0 + "</td>"
                    + "<td>" + Math.round(meanlist[11]*100000)/100000.0 + "</td>"
                    + "</tr>";
                
                $("#movieList").append(html);
                $("#chart").append(div);
                },   
            beforeSend:function(){
                $("#movieList").empty();
                $("#chart").empty();
            },
            error:function(e){  
                alert(e.responseText);  
            }  
        });  
      
    });
}