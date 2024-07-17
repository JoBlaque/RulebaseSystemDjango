
let i = 0;

function rowTemplate(i) {
  return `<tr data-index=${i}>
      <td>${i}</td>
      <td><input type="text" name="name-${i}"></td>
      <td><input type="text" name="phone-${i}"></td>
      <td><input type="text" name="Email-${i}"></td>
      <td><i class="fa fa-times-circle" style="font-size: 22px; color: red;" onclick="removeRow(${i})"></i></td>
    </tr>`
}

for (i = 0; i < 4; i ++) {
  $('tbody').append(rowTemplate(i));
}

function removeRow(i) {
  $("tbody").find(`tr[data-index='${i}']`).remove();
}

function addRow() {
  $('tbody').append(rowTemplate(i));
  i++;
}