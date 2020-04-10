function doGet(e) {

  return HtmlService.createTemplateFromFile("page").evaluate();
  
}

function clicked(result){
  
  Logger.log(result);
  var ss = SpreadsheetApp.openById("1SuYC79hjXU4kTqLkMvezUnbvnnTp9iBd6xjTaIXW5_c").getSheetByName("Sheet1")
//  ss.getRange(ss.getLastRow()+1, 1, 1, 1).setValue(result)
  ss.appendRow([result.fname, result.lname, result.status, new Date()])
}
//var sheet Id = "1SuYC79hjXU4kTqLkMvezUnbvnnTp9iBd6xjTaIXW5_c"

function include(filename){
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}
