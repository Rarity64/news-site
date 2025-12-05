$('body').prepend(
    `<nav class="navbar navbar-expand-xl navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <i class="fa-solid fa-newspaper" style="color: #FFD43B;"></i>
                Новости
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarWithDropdown" aria-controls="navbarWithDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse show" id="navbarWithDropdown">
                <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Главные новости</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Статьи</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Email-рассылка</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
        По темам
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
        <li><a class="dropdown-item" href="#">Россия</a></li>
        <li><a class="dropdown-item" href="#">Весь мир</a></li>
        <li><a class="dropdown-item" href="#">Бывший СССР</a></li>
                    </ul>
                </li>
                </ul>
            </div>
        </div>
    </nav>`
)