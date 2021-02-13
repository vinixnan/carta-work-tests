from test_01.whalesay.plugin import plugin_manager

class Whale(object):

    def talk(self, message_id):
        messages = {}
        entries = plugin_manager.hook.messages()
        for entry in entries:
            for k, v in entry.items():
                messages[k] = v

        message = messages.get(message_id, "Hello!")
        parts = message.split(" ")
        thoughts = []
        chunk_size = 8
        for i in range(int(len(parts)/chunk_size) + 1):
            words = parts[i*chunk_size:i*chunk_size + chunk_size]
            thoughts.append("          " + "  "*i + " ".join(words))
        all_thoughts = "\n".join(thoughts)

        whale = f'''
{all_thoughts}
                    ##         .
              ## ## ##        ==
           ## ## ## ## ##    ===
       /"""""""""""""""""\___/ ===
      {{                       /  ===-
       \______ O           __/
         \    \         __/
          \____\_______/

'''
        return whale