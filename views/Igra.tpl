<html>
    <head>
        <title> Igra </title>
        <style>
            body {
                background-color: antiquewhite;
                font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
            }
            form {
                margin-bottom: 0px;
            }
        </style>
    </head>
    <body>
        <center>
            <p>
                <table>
                    % for i in range(Vrstica):
                        <tr height="30px">
                            % for j in range(Stolpec):
                                % if Polje[i][j] == -2:
                                    <td>
                                        <form method="POST">
                                            <input type="hidden" name="vrstica" value={{i}}></input>
                                            <input type="hidden" name="stolpec" value={{j}}></input>
                                            <input type="image" src="../Slike/Pokrito_polje.png" width="30px" height="30px" value="">
                                        </form>
                                    </td>
                                % elif Polje[i][j] == -1:
                                    <td>
                                        <img src="../Slike/Mina.png" width="30px" height="30px">
                                    </td>
                                % elif Polje[i][j] == 0:
                                    <td>
                                        <img src="../Slike/Prazno_polje.png" width="30px" height="30px">
                                    </td>
                                % elif Polje[i][j] == -3:
                                    <td>
                                        <form method="POST">
                                            <input type="hidden" name="vrstica" value={{i}}></input>
                                            <input type="hidden" name="stolpec" value={{j}}></input>
                                            <input type="image" src="../Slike/Zastava.png" width="30px" height="30px" value="">
                                        </form>
                                    </td>
                                % else:
                                    <td>
                                        <img src="../Slike/{{Polje[i][j]}}.png" widht="30px" height="30px">
                                    </td>
                                % end
                            % end
                        </tr>
                    % end
                </table>
            </p>
            <p>
                <form method="POST">
                    <input type="submit" value="Zastavica"></input>
                </form>
            </p>
            <p> Število preostalih min: {{Mine}} </p>
        </center>
    </body>
</html>