#
# PySNMP MIB module ALTIGA-CAP (http://snmplabs.com/pysmi)
# ASN.1 source ALTIGA-CAP
# Source digest sha256:4a89d6ea3a074b0a9fe436945b7e9f06d625a2fb46f7bcab3b671982acd8d08d
# Produced by pysmi-2.3.0
#
alCapModule, altigaCaps = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alCapModule", "altigaCaps")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
altigaCapModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 2, 1))
altigaCapModule.setRevisions(('2002-09-09 12:00', '2002-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: altigaCapModule.setRevisionsDescriptions(('Updated MIB to comply to Cisco MIB Police standards.\n                 Added missing supports for new Altiga MIBs.\n                ', 'Updated with new header',))
if mibBuilder.loadTexts: altigaCapModule.setLastUpdated('2002-09-09 12:00')
if mibBuilder.loadTexts: altigaCapModule.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: altigaCapModule.setContactInfo('Cisco Systems\n          170 W Tasman Drive\n          San Jose, CA  95134\n          USA\n\n          Tel: +1 800 553-NETS\n          E-mail: cs-cvpn3000@cisco.com')
if mibBuilder.loadTexts: altigaCapModule.setDescription('The Altiga Networks capabilities MIB models counters and\n          objects that are of management interest for networks\n          capabilities.\n         \n          Acronyms\n          The following acronyms are used in this document:\n\n            DHCP:       Dynamic Host Configuration Protocol\n\n            DNS:        Domain Name Service\n\n            FTP:        File Transfer Protocol\n\n            HTTP:       HyperText Transfer Protocol\n\n            ICMP:       Internet Control Message Protocol\n\n            IP:         Internet Protocol\n\n            L2TP:       Layer-2 Tunneling Protocol\n\n            MIB:        Management Information Base\n\n            PPP:        Point-to-Point Protocol\n\n            PPTP:       Point-to-Point Tunneling Protocol\n\n            SEP:        Scalable Encryption Processor\n\n            SNMP:       Simple Network Management Protocol\n\n            SSL:        Secure Sockets Layer\n\n            TCP:        Transmission Control Protocol\n\n            UDP:        User Datagram Protocol\n\n         ')
altigaBasicAgent = AgentCapabilities((1, 3, 6, 1, 4, 1, 3076, 4, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgent = altigaBasicAgent.setProductRelease('Altiga Agent v1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgent = altigaBasicAgent.setStatus('obsolete')
if mibBuilder.loadTexts: altigaBasicAgent.setDescription('Altiga SNMP Agent')
altigaBasicAgentRev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 3076, 1, 1, 2, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgentRev1 = altigaBasicAgentRev1.setProductRelease('Altiga Agent v1.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaBasicAgentRev1 = altigaBasicAgentRev1.setStatus('current')
if mibBuilder.loadTexts: altigaBasicAgentRev1.setDescription('Altiga SNMP Agent')
mibBuilder.exportSymbols("ALTIGA-CAP", PYSNMP_MODULE_ID=altigaCapModule, altigaBasicAgent=altigaBasicAgent, altigaBasicAgentRev1=altigaBasicAgentRev1, altigaCapModule=altigaCapModule)
