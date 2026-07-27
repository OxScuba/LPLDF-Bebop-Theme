/* Visionneuse des fiches produit LPLDF.
   Les miniatures restent gérées par be-BOP ; seule la grande image ouvre ce calque. */
(function () {
  "use strict";

  function initialiseGallery() {
    var productExtra = document.querySelector(".lpldf-product-extra");
    var productMain = productExtra && productExtra.closest("main");
    var displayedImage = productMain && productMain.querySelector(".aspect-video img");

    if (!displayedImage || displayedImage.dataset.lpldfGalleryReady === "true") return;

    displayedImage.dataset.lpldfGalleryReady = "true";
    displayedImage.classList.add("lpldf-gallery-ready");
    displayedImage.setAttribute("role", "button");
    displayedImage.setAttribute("tabindex", "0");
    displayedImage.setAttribute("aria-label", "Agrandir l’image affichée");

    var lightbox = document.createElement("div");
    lightbox.className = "lpldf-image-lightbox";
    lightbox.hidden = true;
    lightbox.setAttribute("role", "dialog");
    lightbox.setAttribute("aria-modal", "true");
    lightbox.setAttribute("aria-label", "Image du produit en grand");
    lightbox.innerHTML =
      '<button class="lpldf-image-lightbox__close" type="button" aria-label="Fermer l’image agrandie">×</button>' +
      '<img class="lpldf-image-lightbox__image" alt="">';
    document.body.appendChild(lightbox);

    var enlargedImage = lightbox.querySelector(".lpldf-image-lightbox__image");
    var closeButton = lightbox.querySelector(".lpldf-image-lightbox__close");
    var previousFocus = null;

    function openLightbox() {
      previousFocus = document.activeElement;
      enlargedImage.src = displayedImage.currentSrc || displayedImage.src;
      enlargedImage.alt = displayedImage.alt || "Image du produit";
      lightbox.hidden = false;
      document.documentElement.classList.add("lpldf-lightbox-open");
      closeButton.focus();
    }

    function closeLightbox() {
      lightbox.hidden = true;
      document.documentElement.classList.remove("lpldf-lightbox-open");
      if (previousFocus && typeof previousFocus.focus === "function") previousFocus.focus();
    }

    displayedImage.addEventListener("click", openLightbox);
    displayedImage.addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        openLightbox();
      }
    });
    closeButton.addEventListener("click", closeLightbox);
    lightbox.addEventListener("click", function (event) {
      if (event.target === lightbox) closeLightbox();
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && !lightbox.hidden) closeLightbox();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialiseGallery, { once: true });
  } else {
    initialiseGallery();
  }
})();
