document.addEventListener("DOMContentLoaded", () => {
    let slideIndex = 0;
    let slides = document.getElementsByClassName("slide");
    let dots = document.getElementsByClassName("dot");
    let autoSlideInterval;

    function showSlide(index) {
        if (slides.length === 0) return;
        slideIndex = (index + slides.length) % slides.length;
        for (let i = 0; i < slides.length; i++) {
            slides[i].classList.remove("active");
            if (dots[i]) dots[i].classList.remove("active");
        }
        slides[slideIndex].classList.add("active");
        if (dots[slideIndex]) dots[slideIndex].classList.add("active");
    }

    function plusSlides(n) {
        showSlide(slideIndex + n);
        resetAutoSlide();
    }

    function currentSlide(n) {
        showSlide(n);
        resetAutoSlide();
    }

    function autoSlide() {
        plusSlides(1);
        autoSlideInterval = setTimeout(autoSlide, 4000);
    }

    function resetAutoSlide() {
        clearTimeout(autoSlideInterval);
        autoSlideInterval = setTimeout(autoSlide, 4000);
    }

    window.plusSlides = plusSlides;
    window.currentSlide = currentSlide;

    showSlide(slideIndex);
    autoSlide();
});

function updateBasketCount(newCount) {
  const basketCount = document.getElementById('basket-count');
  if (basketCount) basketCount.textContent = newCount;
}

document.addEventListener('DOMContentLoaded', function () {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  document.querySelectorAll('.product-card').forEach(card => {
    const productId = card.dataset.productId;
    const addButton = card.querySelector('.add-button');
    let qtyControl = card.querySelector('.qty-control');

    function renderQtyControl(qty) {
      if (!qtyControl) {
        qtyControl = document.createElement('div');
        qtyControl.className = 'qty-control green-qty';
        qtyControl.style.display = 'flex';
        qtyControl.style.alignItems = 'center';
        qtyControl.style.gap = '8px';
        qtyControl.style.margin = '10px 0';
        qtyControl.innerHTML = `
          <button class="qty-btn green-btn" data-action="dec" style="min-width:32px;">−</button>
          <input type="number" class="product-amount__input tw-font-strong" pattern="[0-9]*" min="0" max="50" step="1" value="${qty}" aria-label="Množstvo v košíku" style="width: 48px; text-align: center; font-weight: bold; font-size: 1.1rem; margin: 0 4px;">
          <button class="qty-btn green-btn" data-action="inc" style="min-width:32px;">+</button>
        `;
        addButton.parentNode.replaceChild(qtyControl, addButton);
        setupQtyListeners();
      } else {
        qtyControl.querySelector('input[type=number]').value = qty;
        qtyControl.style.display = 'flex';
      }
    }

    function setupQtyListeners() {
      qtyControl.querySelectorAll('.qty-btn').forEach(btn => {
        btn.addEventListener('click', function () {
          const action = btn.dataset.action;
          fetch('/basket/update-quantity/', {
            method: 'POST',
            headers: {
              'X-CSRFToken': getCookie('csrftoken'),
              'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `produkt_id=${productId}&action=${action}`
          })
          .then(res => res.json())
          .then(data => {
            if (data.success) {
              if (data.new_qty > 0) {
                qtyControl.querySelector('input[type=number]').value = data.new_qty;
              } else {
                qtyControl.style.display = 'none';
                addButton.style.display = 'inline-block';
              }
              if (typeof data.basket_count !== 'undefined') {
                updateBasketCount(data.basket_count);
              }
            }
          });
        });
      });
      // Manuálna zmena inputu
      const input = qtyControl.querySelector('input[type=number]');
      input.addEventListener('change', function () {
        let newQty = parseInt(input.value);
        if (isNaN(newQty) || newQty < 0) newQty = 0;
        if (newQty > 50) newQty = 50;
        fetch('/basket/update-quantity/', {
          method: 'POST',
          headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          body: `produkt_id=${productId}&action=set&quantity=${newQty}`
        })
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            if (data.new_qty > 0) {
              input.value = data.new_qty;
            } else {
              qtyControl.style.display = 'none';
              addButton.style.display = 'inline-block';
            }
            if (typeof data.basket_count !== 'undefined') {
              updateBasketCount(data.basket_count);
            }
          }
        });
      });
    }

    if (addButton) {
      addButton.addEventListener('click', function (e) {
        e.preventDefault();
        fetch(`/basket/pridat/${productId}/`, {
          method: 'POST',
          headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          body: 'quantity=1'
        })
        .then(res => res.json())
        .then(data => {
          if (data.success) {
            renderQtyControl(data.quantity || 1);
            if (typeof data.basket_count !== 'undefined') {
              updateBasketCount(data.basket_count);
            }
          }
        });
    }

    if (qtyControl) {
      setupQtyListeners();
    }
  });
});

