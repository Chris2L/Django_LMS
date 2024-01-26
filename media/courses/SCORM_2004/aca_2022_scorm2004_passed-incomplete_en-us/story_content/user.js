function ExecuteScript(strId)
{
  switch (strId)
  {
      case "5pRg4qlQdtL":
        Script1();
        break;
      case "6p28Ca9d9ue":
        Script2();
        break;
      case "5XovBaKEhRE":
        Script3();
        break;
      case "6N1IjErzc2p":
        Script4();
        break;
      case "5y9scUkNhpU":
        Script5();
        break;
      case "6HA8ge9Ep8a":
        Script6();
        break;
      case "5sg6ly9wY9D":
        Script7();
        break;
      case "5uzsFdzadKA":
        Script8();
        break;
      case "6T5vfcO89D5":
        Script9();
        break;
      case "6Gsw45Hr3VX":
        Script10();
        break;
      case "5ia7EBAA8Pu":
        Script11();
        break;
      case "6Sy8xQIc0yB":
        Script12();
        break;
      case "6DxKrVQ8Ojl":
        Script13();
        break;
      case "6DGTjeB0AKN":
        Script14();
        break;
  }
}

function Script1()
{
  var player = GetPlayer();

function findLMSAPI(win) {
 if (win.hasOwnProperty("GetStudentID")) return win;

  else if (win.parent == win) return null;

  else return findLMSAPI(win.parent);
}

var lmsAPI = findLMSAPI(this);
var myName = lmsAPI.GetStudentName();
var array = myName.split(',');
var newName = array[1]; // you can also try array[1]
player.SetVar("fname", newName);

}

function Script2()
{
  var player = GetPlayer();

function findLMSAPI(win) {
  if (win.hasOwnProperty("GetStudentID")) return win;

  else if (win.parent == win) return null;

  else return findLMSAPI(win.parent);
}

var lmsAPI = findLMSAPI(this);
var myName = lmsAPI.GetStudentName();
var array = myName.split(',');
var newName = array[0]; // you can also try array[1]
player.SetVar("lname", newName);
}

function Script3()
{
  var currentDate = new Date()
var day = currentDate.getDate()
var month = currentDate.getMonth()+1

function getMonthNameFromNumber(monthNumber) 
{
    var monthName = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    return monthName[monthNumber];
}

var monthName = getMonthNameFromNumber(new Date().getMonth());

var monthNameCaps = monthName.toUpperCase();

var year = currentDate.getFullYear();
var player = GetPlayer();
var newName = day + " " + monthNameCaps + ", " +year
player.SetVar("date", newName);

}

function Script4()
{
  window.print();
}

function Script5()
{
  window.print();

}

function Script6()
{
  window.print();

}

function Script7()
{
  window.print();

}

function Script8()
{
  window.print();

}

function Script9()
{
  window.print();

}

function Script10()
{
  window.print();

}

function Script11()
{
  window.print();

}

function Script12()
{
  window.print();

}

function Script13()
{
  window.print();

}

function Script14()
{
  window.print();

}

function getActor() {
  return {
    "objectType": "Agent",
    "account": {
      "homePage": "https://learnsecurity.amazon.com",
      "name": "Random" + Math.floor(Math.random() * Number.MAX_SAFE_INTEGER)
    }
  };
}
