local status_ok, configs = pcall(require, "nvim-treesitter.configs")
if not status_ok then
    return
end

configs.setup {
    ensure_installed = { "c", "vim", "vimdoc", "query" },
    ignore_install = {"php"}, -- List of parsers to ignore installing
    sync_install = false, -- install languages synchronously (only applied to `ensure_installed`)
    highlight = {
        enable = true, -- false will disable the whole extension
        disable = { "" }, -- list of language that will be disabled
        additional_vim_regex_highlighting = true,
    },
    indent = { 
        enable = false, 
    },
    folding = {
        enable = true,
        foldexpr = "nvim_treesitter#foldexpr()",
    },
}
