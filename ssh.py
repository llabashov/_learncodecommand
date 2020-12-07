"""
https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent

Генерация нового SSH-ключа и добавление его в ssh-агент
После того как вы проверили наличие существующих SSH-ключей, вы можете сгенерировать новый SSH-ключ для проверки подлинности, а затем добавить его в ssh-агент.


Если у вас еще нет SSH-ключа, вы должны сгенерировать новый SSH-ключ. Если вы не уверены, есть ли у вас уже SSH-ключ, проверьте наличие существующих ключей.

Если вы не хотите повторно вводить свою парольную фразу каждый раз, когда используете свой SSH-ключ , вы можете добавить свой ключ в SSH-агент, который управляет вашими SSH-ключами и запоминает вашу парольную фразу.

Генерация нового SSH ключа
Откройте Терминал.

Вставьте текст ниже, заменив его на свой адрес электронной почты на GitHub.

$ ssh-keygen -t ed25519 -C "your_email@example.com"
Примечание: Если вы используете устаревшую систему, которая не поддерживает алгоритм Ed25519, используйте:

$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
Это создает новый ssh-ключ, используя предоставленную электронную почту в качестве метки.
> Generating public/private ed25519 key pair.
Когда вам будет предложено ввести файл для сохранения ключа, нажмите клавишу Enter. Здесь принимается расположение файла по умолчанию.

> Enter a file in which to save the key (/Users/you/.ssh/id_ed25519): [Press enter]
В командной строке введите безопасную парольную фразу. Дополнительные сведения см. В разделе "Работа с парольными фразами ключей SSH".

> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
Добавление вашего SSH-ключа в ssh-агент
Перед добавлением нового SSH-ключа в ssh-агент для управления вашими ключами вы должны были проверить наличие существующих SSH-ключей и сгенерировать новый SSH-ключ. При добавлении SSH-ключа в агент используйте ssh-addкоманду macOS по умолчанию , а не приложение , установленное macports, homebrewили каким-либо другим внешним источником.

Запустите ssh-агент в фоновом режиме.

$ eval "$(ssh-agent -s)"
> Agent pid 59566
Если вы используете macOS Sierra 10.12.2 или более позднюю версию, вам нужно будет изменить свой ~/.ssh/configфайл, чтобы автоматически загружать ключи в ssh-агент и хранить парольные фразы в связке ключей.

Во-первых, проверьте, существует ли ваш ~/.ssh/configфайл в папке по умолчанию.

$ open ~/.ssh/config
> The file /Users/you/.ssh/config does not exist.
Если файл не существует, создайте его.

$ touch ~/.ssh/config
Откройте ~/.ssh/configфайл, а затем измените его, заменив ~/.ssh/id_ed25519, если вы не используете расположение и имя id_ed25519ключа по умолчанию.

Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
Добавьте свой закрытый ключ SSH к ssh-агенту и сохраните свою парольную фразу в связке ключей. Если вы создали свой ключ с другим именем или добавляете существующий ключ с другим именем, замените id_rsa в команде именем вашего файла закрытого ключа.

$ ssh-add -K ~/.ssh/id_ed25519
Примечание: эта -Kопция является стандартной версией Applessh-add, которая хранит парольную фразу в вашем брелке для ключей, когда вы добавляете ssh-ключ к ssh-агенту.

Если у вас не установлена стандартная версия Apple, вы можете получить сообщение об ошибке. Дополнительные сведения об устранении этой ошибки см. В разделе "Error: ssh-add: illegal option -- K."

Добавьте SSH-ключ в свою учетную запись GitHub.
"""