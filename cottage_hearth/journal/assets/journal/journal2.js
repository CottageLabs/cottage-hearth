Promise.all([import('react'), import('react-dom')]).then(() => {
    let [React, ReactDOM] = arguments;
    ReactDOM.render(<h1>Hello World</h1>, document.getElementById("root"));
});


