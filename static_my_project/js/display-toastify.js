$(function () {
  let list_items = $(".messages li");

  list_items.each(function (index, element) {
    let toastify_conf = {
      text: $(element).data("message"),
      duration: 3000,
      close: true,
      gravity: "bottom",
      position: "right",
    };

    let level = +$(element).data("level");

    // 10 = DEBUG
    // 20 = INFO
    // 25 = SUCCESS
    // 30 = WARNING
    // 40 = 40
    if (level === 10) {
      toastify_conf.backgroundColor = "#435ebe";
    } else if (level === 20) {
      toastify_conf.backgroundColor = "#0dcaf0";
    } else if (level === 25) {
      toastify_conf.backgroundColor = "#198754";
    } else if (level === 30) {
      toastify_conf.backgroundColor = "#ffc107";
    } else if (level === 40) {
      toastify_conf.backgroundColor = "#dc3545";
    }

    Toastify(toastify_conf).showToast();
  });
});
