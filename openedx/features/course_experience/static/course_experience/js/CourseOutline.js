/* globals Logger */

import { keys } from 'edx-ui-toolkit/js/utils/constants';

// @TODO: Figure out how to make webpack handle default exports when libraryTarget: 'window'
export class CourseOutline {  // eslint-disable-line import/prefer-default-export
  constructor() {
    const focusable = [...document.querySelectorAll('.outline-item.focusable')];

    focusable.forEach(el => el.addEventListener('keydown', (event) => {
      const index = focusable.indexOf(event.target);

      switch (event.key) {  // eslint-disable-line default-case
        case keys.down:
          event.preventDefault();
          focusable[Math.min(index + 1, focusable.length - 1)].focus();
          break;
        case keys.up:  // @TODO: Get these from the UI Toolkit
          event.preventDefault();
          focusable[Math.max(index - 1, 0)].focus();
          break;
      }
    }));

    [...document.querySelectorAll('a:not([href^="#"])')]
      .forEach(link => link.addEventListener('click', (event) => {
        Logger.log(
          'edx.ui.lms.link_clicked',
          {
            current_url: window.location.href,
            target_url: event.currentTarget.href,
          },
        );
      }),
    );

    function expandSection(sectionToggleButton) {
      // PolyFill Array.from() IE11
      if (!Array.from) {
        Array.from = (function () {
          var toStr = Object.prototype.toString;
          var isCallable = function (fn) {
            return typeof fn === 'function' || toStr.call(fn) === '[object Function]';
          };
          var toInteger = function (value) {
            var number = Number(value);
            if (isNaN(number)) { return 0; }
            if (number === 0 || !isFinite(number)) { return number; }
            return (number > 0 ? 1 : -1) * Math.floor(Math.abs(number));
          };
          var maxSafeInteger = Math.pow(2, 53) - 1;
          var toLength = function (value) {
            var len = toInteger(value);
            return Math.min(Math.max(len, 0), maxSafeInteger);
          };

          // The length property of the from method is 1.
          return function from(arrayLike/*, mapFn, thisArg */) {
            // 1. Let C be the this value.
            var C = this;

            // 2. Let items be ToObject(arrayLike).
            var items = Object(arrayLike);

            // 3. ReturnIfAbrupt(items).
            if (arrayLike == null) {
              throw new TypeError('Array.from requires an array-like object - not null or undefined');
            }

            // 4. If mapfn is undefined, then let mapping be false.
            var mapFn = arguments.length > 1 ? arguments[1] : void undefined;
            var T;
            if (typeof mapFn !== 'undefined') {
              // 5. else
              // 5. a If IsCallable(mapfn) is false, throw a TypeError exception.
              if (!isCallable(mapFn)) {
                throw new TypeError('Array.from: when provided, the second argument must be a function');
              }

              // 5. b. If thisArg was supplied, let T be thisArg; else let T be undefined.
              if (arguments.length > 2) {
                T = arguments[2];
              }
            }

            // 10. Let lenValue be Get(items, "length").
            // 11. Let len be ToLength(lenValue).
            var len = toLength(items.length);

            // 13. If IsConstructor(C) is true, then
            // 13. a. Let A be the result of calling the [[Construct]] internal method 
            // of C with an argument list containing the single item len.
            // 14. a. Else, Let A be ArrayCreate(len).
            var A = isCallable(C) ? Object(new C(len)) : new Array(len);

            // 16. Let k be 0.
            var k = 0;
            // 17. Repeat, while k < len… (also steps a - h)
            var kValue;
            while (k < len) {
              kValue = items[k];
              if (mapFn) {
                A[k] = typeof T === 'undefined' ? mapFn(kValue, k) : mapFn.call(T, kValue, k);
              } else {
                A[k] = kValue;
              }
              k += 1;
            }
            // 18. Let putStatus be Put(A, "length", len, true).
            A.length = len;
            // 20. Return A.
            return A;
          };
        }());
      };
      const $toggleButtonChevron = $(sectionToggleButton).children('.fa-chevron-right');
      const $contentPanel = $(document.getElementById(sectionToggleButton.getAttribute('aria-controls')));

      $contentPanel.slideDown();
      $contentPanel.removeClass('is-hidden');
      $toggleButtonChevron.addClass('fa-rotate-90');
      sectionToggleButton.setAttribute('aria-expanded', 'true');
    }

    function collapseSection(sectionToggleButton) {
      // PolyFill Array.from() IE11
      if (!Array.from) {
        Array.from = (function () {
          var toStr = Object.prototype.toString;
          var isCallable = function (fn) {
            return typeof fn === 'function' || toStr.call(fn) === '[object Function]';
          };
          var toInteger = function (value) {
            var number = Number(value);
            if (isNaN(number)) { return 0; }
            if (number === 0 || !isFinite(number)) { return number; }
            return (number > 0 ? 1 : -1) * Math.floor(Math.abs(number));
          };
          var maxSafeInteger = Math.pow(2, 53) - 1;
          var toLength = function (value) {
            var len = toInteger(value);
            return Math.min(Math.max(len, 0), maxSafeInteger);
          };

          // The length property of the from method is 1.
          return function from(arrayLike/*, mapFn, thisArg */) {
            // 1. Let C be the this value.
            var C = this;

            // 2. Let items be ToObject(arrayLike).
            var items = Object(arrayLike);

            // 3. ReturnIfAbrupt(items).
            if (arrayLike == null) {
              throw new TypeError('Array.from requires an array-like object - not null or undefined');
            }

            // 4. If mapfn is undefined, then let mapping be false.
            var mapFn = arguments.length > 1 ? arguments[1] : void undefined;
            var T;
            if (typeof mapFn !== 'undefined') {
              // 5. else
              // 5. a If IsCallable(mapfn) is false, throw a TypeError exception.
              if (!isCallable(mapFn)) {
                throw new TypeError('Array.from: when provided, the second argument must be a function');
              }

              // 5. b. If thisArg was supplied, let T be thisArg; else let T be undefined.
              if (arguments.length > 2) {
                T = arguments[2];
              }
            }

            // 10. Let lenValue be Get(items, "length").
            // 11. Let len be ToLength(lenValue).
            var len = toLength(items.length);

            // 13. If IsConstructor(C) is true, then
            // 13. a. Let A be the result of calling the [[Construct]] internal method 
            // of C with an argument list containing the single item len.
            // 14. a. Else, Let A be ArrayCreate(len).
            var A = isCallable(C) ? Object(new C(len)) : new Array(len);

            // 16. Let k be 0.
            var k = 0;
            // 17. Repeat, while k < len… (also steps a - h)
            var kValue;
            while (k < len) {
              kValue = items[k];
              if (mapFn) {
                A[k] = typeof T === 'undefined' ? mapFn(kValue, k) : mapFn.call(T, kValue, k);
              } else {
                A[k] = kValue;
              }
              k += 1;
            }
            // 18. Let putStatus be Put(A, "length", len, true).
            A.length = len;
            // 20. Return A.
            return A;
          };
        }());
      };
      const $toggleButtonChevron = $(sectionToggleButton).children('.fa-chevron-right');
      const $contentPanel = $(document.getElementById(sectionToggleButton.getAttribute('aria-controls')));

      $contentPanel.slideUp();
      $contentPanel.addClass('is-hidden');
      $toggleButtonChevron.removeClass('fa-rotate-90');
      sectionToggleButton.setAttribute('aria-expanded', 'false');
    }

    [...document.querySelectorAll(('.accordion'))]
      .forEach((accordion) => {
        const sections = Array.prototype.slice.call(accordion.querySelectorAll('.accordion-trigger'));

        sections.forEach(section => section.addEventListener('click', (event) => {
          const sectionToggleButton = event.currentTarget;
          if (sectionToggleButton.classList.contains('accordion-trigger')) {
            const isExpanded = sectionToggleButton.getAttribute('aria-expanded') === 'true';
            if (!isExpanded) {
              expandSection(sectionToggleButton);
            } else if (isExpanded) {
              collapseSection(sectionToggleButton);
            }
            event.stopImmediatePropagation();
          }
        }));
      });

    const toggleAllButton = document.querySelector('#expand-collapse-outline-all-button');
    const toggleAllSpan = document.querySelector('#expand-collapse-outline-all-span');
    const extraPaddingClass = 'expand-collapse-outline-all-extra-padding';
    toggleAllButton.addEventListener('click', (event) => {
      const toggleAllExpanded = toggleAllButton.getAttribute('aria-expanded') === 'true';
      let sectionAction;
      if (toggleAllExpanded) {
        toggleAllButton.setAttribute('aria-expanded', 'false');
        sectionAction = collapseSection;
        toggleAllSpan.classList.add(extraPaddingClass);
        toggleAllSpan.innerText = 'Expand All';
      } else {
        toggleAllButton.setAttribute('aria-expanded', 'true');
        sectionAction = expandSection;
        toggleAllSpan.classList.remove(extraPaddingClass);
        toggleAllSpan.innerText = 'Collapse All';
      }
      const sections = Array.prototype.slice.call(document.querySelectorAll('.accordion-trigger'));
      sections.forEach((sectionToggleButton) => {
        sectionAction(sectionToggleButton);
      });
      event.stopImmediatePropagation();
    });
  }
}
