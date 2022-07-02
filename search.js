const data = [
  {
    Homestay_id: 0,
    Homestay_name: "Shivapuri Homestay",
    Homestay_location: "Sundarijal",
    Homestay_capacity: 5,
    Homestay_price: 1230.0,
  },
  {
    Homestay_id: 1,
    Homestay_name: "Vedetar Homestay",
    Homestay_location: "Dharan",
    Homestay_capacity: 6,
    Homestay_price: 1200.0,
  },
  {
    Homestay_id: 2,
    Homestay_name: "Biratnagar Homestay",
    Homestay_location: "Biratnagar",
    Homestay_capacity: 20,
    Homestay_price: 620.6,
  },
];

const searchResults = document.getElementById("search-results");

function createItem() {
  
  data.map((item) => {
    // console.log(item);

    var li_name = document.createElement("li");
    var li_location = document.createElement("li");
    var li_capacity = document.createElement("li");
    var li_price = document.createElement("li");
    var ul = document.createElement("ul");


    item_id = item["Homestay_id"];
    item_name = item["Homestay_name"];
    item_location = item["Homestay_location"];
    item_capacity = item["Homestay_capacity"];
    item_price = item["Homestay_price"];

    ul.setAttribute("id", item_id);
    ul.setAttribute("class","search-component-style");
    li_name.innerHTML = item_name;
    ul.appendChild(li_name);
    li_location.innerHTML = item_location;
    ul.appendChild(li_location);
    li_capacity.innerHTML = item_capacity;
    ul.appendChild(li_capacity);
    li_price.innerHTML = item_price;
    ul.appendChild(li_price);

    searchResults.appendChild(ul);
  });
}
createItem();
