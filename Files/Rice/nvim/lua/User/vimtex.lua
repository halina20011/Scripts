-- yay -S okular
-- pip install neovim-remote
-- yay -S latexrun-git
-- yay -Si texlive-bin

vim.cmd([[syntax enable]])
vim.cmd([[let g:vimtex_view_general_viewer = 'okular']])
vim.cmd([[let g:vimtex_view_general_options = '--unique file:@pdf\#src:@line@tex']])
vim.cmd([[let g:vimtex_compiler_method = 'latexrun']])
-- vim.cmd([[let maplocalleader = ","]])

-- local status_ok, comment = pcall(require, "vimtex")
-- if not status_ok then
--     return
-- end
-- --
-- function vimtex()
--     vim.g.vimtex_view_general_viewer = 'okular'
--     vim.g.vimtex_view_general_options = [[--unique file:@pdf\#src:@line@tex]]
--     vim.g.vimtex_view_method = 'okular'
--     vim.g.vimtex_compiler_latexmk_engines = {
--         _ = '-latexrun'
--     }
--     vim.g.tex_comment_nospell = 1
--     -- vim.g.vimtex_compiler_progname = 'nvr'
--     -- vim.g.vimtex_view_general_options_latexmk = '--unique'
-- end
