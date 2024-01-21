-- local servers = {}
local servers = {
    "html",
    -- "denols", -- diagnostic (custom setup is down)
    "tsserver", -- highlightlighting, cmp 
    -- "clangd",
    "cssls",
    -- "csharp_ls",
    "texlab",
    -- "stylelint_lsp",
	"pyright",
	"jsonls",
}

local settings = {
	ui = {
		border = "none",
		icons = {
			package_installed = "◍",
			package_pending = "◍",
			package_uninstalled = "◍",
		},
	},
	log_level = vim.log.levels.INFO,
	max_concurrent_installers = 4,
}

require("mason").setup(settings)
require("mason-lspconfig").setup({
	ensure_installed = servers,
	automatic_installation = true,
})

local lspconfig_status_ok, lspconfig = pcall(require, "lspconfig")
if not lspconfig_status_ok then
	return
end

local opts = {}
lspconfig.denols.setup{
    -- root_dir = lspconfig.util.root_pattern('deno.json', 'deno.jsonc'),
    on_attach = on_attach,
    single_file_support=true,
    capabilities = capabilities,
};


lspconfig.clangd.setup{
    cmd = { "clangd", "--background-index", "--enable-config"},
    filetypes = { "c", "cpp", "objc", "objcpp" },
}

-- lspconfig.clangd.setup{
--     cmd = {"clangd", "--background-index", "-I/usr/avr/include/"},
--     filetypes = {"c"},
--     -- extraArgs = {
--     --     "-I/usr/avr/include/"
--     -- }
-- }
--
for _, server in pairs(servers) do
	opts = {
        on_attach = require("User.lsp.handlers").on_attach,
        capabilities = require("User.lsp.handlers").capabilities,
    }

	server = vim.split(server, "@")[1]

	local require_ok, conf_opts = pcall(require, "User.lsp.settings." .. server)
	if require_ok then
        opts = vim.tbl_deep_extend("force", conf_opts, opts)
    end

    lspconfig[server].setup(opts)
end
