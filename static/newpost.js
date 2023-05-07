const bidCheckboxes = document.getElementsByClassName("bid");
function handleBidCheckboxClick(event) {
  checkboxes.forEach((checkbox) => {
    if (checkbox !== event.target) {
      checkbox.checked = false;
    }
  });
}
bidCheckboxes.forEach((checkbox) => {
  checkbox.addEventListener("click", handleBidCheckboxClick);
});
