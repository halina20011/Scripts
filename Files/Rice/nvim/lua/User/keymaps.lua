local opts = { noremap = true, silent = true }
local optsVer = { noremap = true, silent = false }

local term_opts = { silent = true }
local keymap = vim.api.nvim_set_keymap

-- Remap space as leader key
keymap("", "<Space>", "<Nop>", opts)
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- <C>      Ctrl
-- <CR>     Carriage return

-- Modes
--   normal_mode = "n",
--   insert_mode = "i",
--   visual_mode = "v",
--   visual_block_mode = "x",
--   term_mode = "t",
--   command_mode = "c",

-- Normal --
-- Better window navigation
keymap("n", "<C-h>", "<C-w>h", optsVer)
keymap("n", "<C-j>", "<C-w>j", optsVer)
keymap("n", "<C-k>", "<C-w>k", optsVer)
keymap("n", "<C-l>", "<C-w>l", optsVer)

-- Split
-- keymap("n", "<C-v>", ":vsplit<CR>", optsVer)

-- Lex = Lexplore
keymap("n", "<leader>e", ":Lex 30<cr>", opts)

-- Resize with arrows
keymap("n", "<C-Up>", ":resize +2<CR>", opts)
keymap("n", "<C-Down>", ":resize -2<CR>", opts)
keymap("n", "<C-Left>", ":vertical resize -2<CR>", opts)
keymap("n", "<C-Right>", ":vertical resize +2<CR>", opts)

-- Navigate buffers
keymap("n", "<S-l>", ":bnext<CR>", opts)
keymap("n", "<S-h>", ":bprevious<CR>", opts)

-- Insert --
-- Press jk fast to exit
keymap("i", "jk", "<ESC>", opts)
-- move with ctrl+h/j/k/l as with arrows
keymap("i", "<C-h>", "<C-left>", opts)
keymap("i", "<C-l>", "<C-right>", opts)
keymap("i", "<C-j>", "<down>", opts)
keymap("i", "<C-k>", "<up>", opts)

-- Visual --
-- Stay in indent mode
keymap("v", "<", "<gv", opts)
keymap("v", ">", ">gv", opts)

-- Move text up and down
keymap("n", "<A-j>", ":m .+1<CR>==", opts)
keymap("n", "<A-k>", ":m .-2<CR>==", opts)

keymap("n", "<S-A-j>", ":m .+1<CR>==", opts)
keymap("n", "<S-A-k>", ":m .-2<CR>==", opts)

-- Visual Block --
-- Move text up and down
keymap("x", "J", ":move '>+1<CR>gv-gv", opts)
keymap("x", "K", ":move '<-2<CR>gv-gv", opts)
keymap("x", "<A-j>", ":move '>+1<CR>gv-gv", opts)
keymap("x", "<A-k>", ":move '<-2<CR>gv-gv", opts)

-- Terminal --
-- Better terminal navigation
keymap("t", "<C-h>", "<C-\\><C-N><C-w>h", term_opts)
keymap("t", "<C-j>", "<C-\\><C-N><C-w>j", term_opts)
keymap("t", "<C-k>", "<C-\\><C-N><C-w>k", term_opts)
keymap("t", "<C-l>", "<C-\\><C-N><C-w>l", term_opts)

-- Comment
-- / == _ ?
keymap("n", "<C-_>", "gcc", term_opts)
keymap("v", "<C-_>", "gc", term_opts)

keymap("n", "tt", ":tabnew<CR>", term_opts)

function _G.tagFunction()
    local word = vim.fn.expand("<cword>")
    vim.cmd("tag " .. word)
end

keymap("n", "T", ":lua tagFunction()<CR>", opts)

function showMessage(message)
    vim.cmd("echo \"" .. vim.fn.fnameescape(message) .. "\"")
end

local tC = table.concat

function getVisualSelection()
    local sStart = vim.fn.getpos("'<")
    local sEnd = vim.fn.getpos("'>")
    local startLine = sStart[2]
    local endLine = sEnd[2]

    local lines = vim.api.nvim_buf_get_lines(0, startLine - 1, endLine, false)
    local text = table.concat(lines, "")
    showMessage("lines >" .. table.concat(lines, "\n"))
    showMessage("from " .. table.concat(sStart, " ") )
    showMessage("to " .. table.concat(sEnd, " ") )

    -- sub(string, from, to)
    lines[1] = string.sub(lines[1], sStart[3])

    local beforeSel = vim.api.nvim_buf_get_lines(0, startLine - 1, startLine, false)[1]
    local afterSel = vim.api.nvim_buf_get_lines(0, endLine, endLine + 1, false)[1]

    return beforeSel, table.concat(lines, "\n"), afterSel
end

function _G.reverseSelected()
    local beforeSel, selectedText, afterSel = getVisualSelection()
    local reverseSelectedText = string.reverse(selectedText)

    showMessage("before " .. beforeSel)
    showMessage("selected " .. selectedText)
    showMessage("after " .. afterSel)

    local sStart = vim.fn.getpos("'<")
    local sEnd = vim.fn.getpos("'>")

    local startLine = sStart[2]
    local endLine = sEnd[2]

    local newText = vim.split(beforeSel .. reverseSelectedText .. afterSel, "\n")
    local lines = vim.api.nvim_buf_set_lines(0, startine - 1, endLine, false, newText)
end

keymap("v", "R", ":lua reverseSelected()<CR>", opts)
