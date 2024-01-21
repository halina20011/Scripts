-- For more options write type ":help options"

local options = {
    backup = false,                        -- creates a backup file
    swapfile = true,                       -- creates a swapfile
    writebackup = true,                    -- if a file is being used by another process, it is not allowed to be edited

    clipboard = "unnamedplus",              -- allows neovim to access the system clipboard
    -- vim.opt.cmdheight = 2,                  -- more space in the neovim command line for displaying messages
    completeopt = { "menuone", "noselect" },-- mostly just for cmp
    conceallevel = 0,                       -- so that `` is visible in markdown files
    fileencoding = "utf-8",                 -- the encoding written to a file
    formatoptions = "l",
    linebreak = true,
    breakindent = true,
    
    hlsearch = true,                        -- highlight all matches on previous search pattern
    ignorecase = false,                      -- ignore case in search patterns
    mouse = "v",                            -- allow the mouse to be used in neovim
    -- pumheight = 10,                         -- pop up menu height
    -- showmode = false,                       -- we don't need to see things like -- INSERT -- anymore
    smartcase = false,                       -- smart case
    smartindent = false,                     -- make indenting smarter again
    smarttab = false,

    splitbelow = true,                      -- force all horizontal splits to go below current window
    splitright = true,                      -- force all vertical splits to go to the right of current window

    termguicolors = true,                   -- set term gui colors (most terminals support this)
    timeoutlen = 500,                      -- time to wait for a mapped sequence to complete (in milliseconds)
    undofile = true,                        -- enable persistent undo
    updatetime = 300,                       -- faster completion (4000ms default)

    -- Tabs
    expandtab = true,                       -- convert tabs to spaces
    showtabline = 2,                        -- always show tabs
    shiftwidth = 4,                         -- the number of spaces inserted for each indentation
    tabstop = 4,                            -- insert 4 spaces for a tab

    cursorline = true,                      -- highlight the current line
    number = true,                          -- set numbered lines
    relativenumber = true,                  -- set relative numbered lines
    numberwidth = 2,                        -- set number column width to 2 {default 4}
    signcolumn = "yes",                     -- always show the sign column, otherwise it would shift the text each time
    wrap = true,                            -- display lines as one long line

    scrolloff = 6,                          -- limit on cursor position when scrolling down 
    sidescrolloff = 6,                      -- when scrolling up

    guifont = "monospace:h17",              -- the font used in graphical neovim applications
    foldlevelstart = 0,
    -- foldmethod="syntax",
    foldmethod = "expr",
    foldexpr = "nvim_treesitter#foldexpr()",
    -- foldlevelstart=99,
    foldcolumn = "1",
}

for k, v in pairs(options) do
    vim.opt[k] = v
end

vim.opt.shortmess:append "c"

vim.cmd "set whichwrap+=<,>,[,],h,l"
vim.cmd [[set iskeyword+=-]]
vim.cmd [[set formatoptions-=cro]] -- TODO: this doesn't seem to work
vim.cmd [[set nofoldenable]]
