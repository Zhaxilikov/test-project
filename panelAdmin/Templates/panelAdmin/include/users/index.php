<?php
session_start();
include '../../path.php';
include '../../app/controllers/users.php';
?>
<!DOCTYPE html>
<html>

<head>
    <?php include("../temp/admin_head.php");?>
</head>

<body>

<div class="page">
    <div class="container__block">

        <!-------------------------header------------------------>
        <?php include("../temp/admin_header.php");?>
        <!-------------------------header end------------------------>

        <!-------------------------sidebar------------------------>
        <?php include("../temp/admin_sidebar.php");?>
        <!-------------------------sidebar end------------------------>

        <!-------------------------main----------------------------->
        <main class="main">
            <div class="container">
                <div class="post">
                    <a class="btn--red btn--rounded btn" href="created.php">Cоздать</a>
                    <a class="btn--blue btn--rounded btn" href="index.php">Редактировать</a>

                    <div class="post__content">
                        <h1>Управление пользователями</h1>
                        <table class="content__table">
                            <tr class="table__inner">
                                <th class="table__title">ID</th>
                                <th class="table__title">Логин</th>
                                <th class="table__title">e-mail</th>
                                <th class="table__title">Роль</th>
                                <th colspan="2" class="table__title">управление</th>
                                <th class="table__title">Дата создание</th>

                            </tr>
                            <?php foreach ($users as $key => $user):?>
                            <tr class="table__inner">
                                <td class="table__item"><?=$user['id']; ?></td>
                                <td class="table__item"><?=$user['username']; ?></td>
                                <td class="table__item"><?=$user['email']; ?></td>
                                <?php if ($user['admin'] == 1):?>
                                <td class="table__item">Админ</td>
                                <?php else:?>
                                <td class="table__item">пользователь</td>
                                <?php endif;?>
                                <td class="table__item"><a href="edit.php?edit_id=<?=$user['id']?>">edit</a></td>
                                <td class="table__item"><a href="index.php?delete_id=<?=$user['id']?>">delete</a></td>
                                <td class="table__item"><a href="#">2023-01-30 09:00</a></td>
                            </tr>
                            <?php endforeach;?>
                        </table>
                    </div>
                    <div class="post__footer">
                        <ul class="post__data">
                            <li class="post__data-item">
                                <time datetime="2022-11-10 10:02">10.11.2022</time>

                            </li>
                        </ul>
                    </div>

                </div>
            </div>
        </main>


        <!-------------------------main end----------------------------->
    </div>

</div>



</body>

</html>

