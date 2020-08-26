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
                            <input type="submit" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Minesweeper_unopened_square.svg/1024px-Minesweeper_unopened_square.svg.png" width="30px" height="30px" value="">
                        </form>
                    </td>
                % elif Polje[i][j] == -1:
                    <td>
                        <img src="https://icon-library.com/images/explosion-icon-png/explosion-icon-png-21.jpg" alt="mina" width="30px" height="30px">
                    </td>
                % elif Polje[i][j] == 0:
                    <td>
                        <img src="https://www.beautycolorcode.com/cdcdcd-200x200.png" alt="prazno" width="30px" height="30px">
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

<label class="switch">
    <input type="checkbox" name="stikalo">
    <span class="slider"></span>
  </label><br><br>
  