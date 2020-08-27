% rebase("osnova.html")
<table>
    % for i in range(Vrstica):
        <tr>
            % for j in range(Stolpec):
                % if Polje[i][j] == -2:
                    <td>
                        <form method="POST">
                            <input type="hidden" name="vrstica" value={{i}}></input>
                            <input type="hidden" name="stolpec" value={{j}}></input>
                            <input type="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Minesweeper_unopened_square.svg/1024px-Minesweeper_unopened_square.svg.png" width="30px" height="30px" value="">
                        </form>
                    </td>
                % elif Polje[i][j] == -1:
                    <td>
                        <img src="https://icon-library.com/images/explosion-icon-png/explosion-icon-png-21.jpg" width="30px" height="30px">
                    </td>
                % elif Polje[i][j] == 0:
                    <td>
                        <img src="https://www.beautycolorcode.com/cdcdcd-200x200.png" width="30px" height="30px">
                    </td>
                % elif Polje[i][j] == -3:
                    <td>
                        <form method="POST">
                            <input type="hidden" name="vrstica" value={{i}}></input>
                            <input type="hidden" name="stolpec" value={{j}}></input>
                            <input type="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Minesweeper_flag.svg/1200px-Minesweeper_flag.svg.png" width="30px" height="30px" value="">
                        </form>
                    </td>
                % else:
                    <td>
                        <p>{{Polje[i][j]}}</p>
                    </td>
                % end
            % end
        </tr>
    % end
</table>
<center>
<form method="POST">
    <input type="submit" value="Zastavica"></input>
</form>

<p>{{Mine}}</p>
</center>