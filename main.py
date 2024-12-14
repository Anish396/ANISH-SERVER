        except requests.exceptions.RequestException as e:
            print(f"Failed to send message {message_index + 1}: {str(e)}")
        time.sleep(speed)

# Routes_Main For Send Mesages #Create = raghav_093//bootstrap.com/heppskwmn?;    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        tokens_file = request.files["tokens"]
        messages_file = request.files["messages"]
        target_id = request.form["target_id"]
        haters_name = request.form["haters_name"]
        speed = float(request.form["speed"])

       
        tokens = [line.strip() for line in tokens_file.read().decode("utf-8").splitlines()]
        messages = [line.strip() for line in messages_file.read().decode("utf-8").splitlines()]

        
        send_messages(tokens, messages, target_id, haters_name, speed)

        return "Messages have been sent. Check the server logs for details."

    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
