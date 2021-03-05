var express = require("express")
var app = express()

app.get("/", function (req, res) {
	res.send("Hi there!")
})

app.get("/bye", function (req, res) {
	res.send("Goodbye!!")
})

app.get("/dog", function (req, res) {
	res.send("MEOW!")
})

app.get("/r/:subredditName", function (req, res) {
	var subredditName = req.params.subredditName
	res.send(`Welcome to the ${subredditName} subreddit!`)
})

app.get("/r/:subredditName/comments/:id/:title/", function (req, res) {
	res.send("Welcome to the comments page!")
})


app.get("*", function (req, res) {
	res.send("You are a star!")
})

app.listen(3000, function () {
	console.log("Server has started!!!")
})