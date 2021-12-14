(function() {

    const URL = 'http://127.0.0.1:5000'

    window.addEventListener('load', setUp)

    function setUp() {
        document.getElementById('create-category').addEventListener('click', foo);
    }

    function foo() {
        let category = document.getElementById('category-name').value;
        let url = 'http://127.0.0.1:5000/category';
        let data = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors'
        };
        fetch(url, data)
        .then(function(response) {
            console.log(response.type)
            return response.text();
        })
        .then(function(response) {
            console.log(response)
        });
    }

    function createCategory() {
        let category = document.getElementById('category-name').value;
        let url = 'http://127.0.0.1:5000/category';
        let data = {
            method: 'POST',
            body: JSON.stringify({
                'category': category
            }),
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'no-cors'
        };
        fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            mode: 'no-cors',
            body: JSON.stringify({
                'category': category
            })
        })
            .then(function(response) {
                return response.json();
            })
            .then(function(response) {
                console.log(response)
            });
    }

}) ();
