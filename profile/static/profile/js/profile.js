(function () {
  const form = document.getElementById("profile-photo-form");
  const input = document.getElementById("profile-photo-input");
  const chooseButton = document.getElementById("choose-photo");
  const preview = document.getElementById("profile-photo-preview");
  const actions = document.getElementById("upload-actions");
  const nameLabel = document.getElementById("selected-photo-name");
  const cancelButton = document.getElementById("cancel-photo");

  if (!form || !input || !chooseButton || !preview || !actions) return;

  const savedImage = preview.src;

  chooseButton.addEventListener("click", function () {
    input.click();
  });

  input.addEventListener("change", function () {
    const file = input.files && input.files[0];
    if (!file) return;
    if (!file.type.startsWith("image/")) {
      input.value = "";
      nameLabel.textContent = "Choose an image file";
      actions.hidden = false;
      return;
    }
    preview.src = URL.createObjectURL(file);
    nameLabel.textContent = file.name;
    actions.hidden = false;
  });

  cancelButton.addEventListener("click", function () {
    form.reset();
    preview.src = savedImage;
    actions.hidden = true;
  });
})();
