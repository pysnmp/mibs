#
# PySNMP MIB module LINKSYS-3SW2SWTABLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source LINKSYS-3SW2SWTABLES-MIB
# Source digest sha256:db4abf216525e0587cd0229571d3c5a06f3498a15a11d3bfa899c6a3b0d6eac3
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rl3sw2swTables = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 63))
rl3sw2swTables.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rl3sw2swTables.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rl3sw2swTables.setLastUpdated('2007-01-02 00:00')
if mibBuilder.loadTexts: rl3sw2swTables.setOrganization('\n                              Linksys LLC.')
if mibBuilder.loadTexts: rl3sw2swTables.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rl3sw2swTables.setDescription('This private MIB module defines 3sw 2sw Tables private MIBs.')
rl3sw2swTablesPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 63, 1), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rl3sw2swTablesPollingInterval.setStatus('current')
if mibBuilder.loadTexts: rl3sw2swTablesPollingInterval.setDescription('The polling interval for dynamic 3SW/2SW tables in seconds.')
mibBuilder.exportSymbols("LINKSYS-3SW2SWTABLES-MIB", PYSNMP_MODULE_ID=rl3sw2swTables, rl3sw2swTables=rl3sw2swTables, rl3sw2swTablesPollingInterval=rl3sw2swTablesPollingInterval)
