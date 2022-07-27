export class CommentComponent {
    constructor(data) {
        this.card = document.createElement('div');
        this.header = document.createElement('div');
        this.body = document.createElement('div');

        this.initComment(data);
    }

    initComment(data) {
        this.card.classList.add('card', 'shadow', 'p-3', 'mb-5', 'bg-body', 'rounded');
        this.header.classList.add('card-header');
        this.body.classList.add('card-body');

        this.setHeader(data);
        this.setBody(data);
    }

    setHeader(data) {
        this.header.innerText = data.author_id;
        this.card.appendChild(this.header);
    }

    setBody(data) {
        const bq = document.createElement('blockquote');
        bq.classList.add('blockquote', 'mb-0');

        const content = document.createElement('p');
        const commentDate = document.createElement('footer');
        commentDate.classList.add('blockquote-footer', 'mt-1');
        content.innerText = data.content;
        commentDate.innerText = "27/07/22";

        bq.appendChild(content);
        bq.appendChild(commentDate);

        this.body.appendChild(bq);
        this.card.appendChild(this.body);
    }
}