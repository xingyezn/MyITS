
 function clicks(q_num,num){
	var my_select = document.getElementById("select"+ q_num + "_" + num);
	var my_button = document.getElementById("value"+ q_num + "_" + num);
	if (my_select.style.display == 'block'){
		return 0;
	}
	var all_num = [5,3,1,0]
	value = 0
	for(i=1;i<=4;i++){
		var one_select = document.getElementById("select"+ q_num+ "_" +i);
		if(one_select.style.display == 'block'){
			value += 1;
		}
	}
	if (value == 4){
		return 0;
	}
	my_select.style.display = 'block';
	my_select.innerHTML = "<span class=\"inner\">"+ all_num[value] + "</span>";
	my_button.value = all_num[value];
	//console.log('选中');
	if (value==2){
		for(i=1;i<=4;i++){
		var one_select = document.getElementById("select"+ q_num+ "_" +i);
		if(one_select.style.display == 'none'){
			one_select.style.display = 'block';
			one_select.innerHTML = "<span class=\"inner\">"+ all_num[value+1] + "</span>";
			var one_button = document.getElementById("value"+ q_num + "_" + i);
			one_button.value = all_num[value+1];
		}
	}
	var select0 = document.getElementById("select"+q_num+"_0");
		select0.style.display = 'block';
		//console.log('test')
	}
 }
 
 function myclear(q_num){
	console.log('清除');
	 for(i=1;i<=4;i++){
		 var clear_select = document.getElementById("select"+ q_num + "_" +i);
		 clear_select.style.display = 'none';
		 var my_button = document.getElementById("value"+ q_num + "_" + i);
		 my_button.value = 100;
	 }
	 var select0 = document.getElementById("select"+q_num+"_0");
	 select0.style.display = 'none';
 }

function submit_data() {
	for (i=1;i<=25;i++){
		for(j=1;j<=4;j++){
			var my_button = document.getElementById("value"+ i + "_" + j);
			//console.log(my_button.value)
			if(my_button.value == 100){
				//location.href = "#question" + i;
				//alert('还有题目没有完成！请完成所有题目！');
				//return 0;
			}
		}
	}
	var SF = 0;
	var ST = 0;
	var NT = 0;
	var NF = 0;
	for(j=1;j<=25;j++){
		var one_SF = document.getElementsByName("SF"+j);
		SF = SF + parseInt(one_SF[0].value);

		var one_ST = document.getElementsByName("ST"+j);
		ST = ST + parseInt(one_ST[0].value);

		var one_NT = document.getElementsByName("NT"+j);
		NT = NT + parseInt(one_NT[0].value);

		var one_NF = document.getElementsByName("NF"+j);
		NF = NF + parseInt(one_NF[0].value);
	}
	var SF_b = document.getElementById("SF");
	SF_b.value = SF;

	var ST_b = document.getElementById("ST");
	ST_b.value = ST;

	var NT_b = document.getElementById("NT");
	NT_b.value = NT;

	var NF_b = document.getElementById("NF");
	NF_b.value = NF;
	/*
	console.log(SF);
	console.log(ST);
	console.log(NT);
	console.log(NF);*/
	alert("你的SF得分为"+SF + ";你的ST得分为" + ST + ";你的NT得分为" + NT + ";你的NF得分为" + NF + ";")
    var question_form = document.getElementById('question_form');
    question_form.submit();
    //question_form.action="{{ url_for('index') }}"
}