export class CommentComponent {
    constructor(data, user_id) {
        this.card = document.createElement('div');
        this.header = document.createElement('div');
        this.body = document.createElement('div');

        this.initComment(data, user_id);
    }

    initComment(data, user_id) {
        this.card.classList.add('card', 'shadow', 'p-3', 'mb-3', 'bg-body', 'rounded');
        this.card.id = data.comment_id;
        this.header.classList.add('card-header');
        this.body.classList.add('card-body');

        this.setHeader(data);
        this.setBody(data, user_id); 
    }

    setHeader(data) {
        this.header.innerText = data.author_name;
        this.card.appendChild(this.header);
    }

    setBody(data, user_id) {
        const bq = document.createElement('blockquote');
        bq.classList.add('blockquote', 'mb-0');

        const content = document.createElement('p');
        const commentDate = document.createElement('footer');
        commentDate.classList.add('blockquote-footer');
        content.innerText = data.content;
        commentDate.innerText = data.create_date;

        bq.appendChild(content);
        bq.appendChild(commentDate);

        this.body.appendChild(bq);
        this.setActions(data, user_id);
        this.card.appendChild(this.body);
    }

    setActions(data, user_id) {
        let userId = parseInt(user_id);
        if (userId == data.author_id) {
            let btnGroup = document.createElement('div');
            btnGroup.classList.add('btn-group', 'mt-2');

            let editBtn = document.createElement('button');
            editBtn.classList.add('btn', 'btn-link', 'text-dark', 'editButton');
            editBtn.innerText = 'edit';

            let deleteBtn = document.createElement('button');
            deleteBtn.classList.add('btn', 'btn-link', 'text-dark', 'deleteButton');
            deleteBtn.innerText = 'delete';

            btnGroup.appendChild(editBtn);
            btnGroup.appendChild(deleteBtn);

            this.body.appendChild(btnGroup);
        }
    }
}