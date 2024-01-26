function ExecuteScript(strId)
{
  switch (strId)
  {
      case "5xmuZP2GpUZ":
        Script1();
        break;
      case "5bYgOg1rT9u":
        Script2();
        break;
      case "6YPVmzP5FVH":
        Script3();
        break;
      case "6CFOiaCMdXt":
        Script4();
        break;
      case "6HCOBryynx2":
        Script5();
        break;
      case "5sgEkgHOiBt":
        Script6();
        break;
      case "5XQgGblVVFV":
        Script7();
        break;
      case "5a1LFz8owkH":
        Script8();
        break;
      case "6aErMwg2wlQ":
        Script9();
        break;
      case "5V3cSodJFcQ":
        Script10();
        break;
      case "6l0f2ZD6CsF":
        Script11();
        break;
      case "67ZRtSWTNPf":
        Script12();
        break;
      case "6GJ0Chh7540":
        Script13();
        break;
      case "6TtdXPOThip":
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
