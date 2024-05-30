#
# PySNMP MIB module MCAFEE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-SMI
# Produced by pysmi-1.1.12 at Thu May 30 02:19:31 2024
# On host fv-az1567-87 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, IpAddress, Gauge32, Counter64, iso, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, TimeTicks, Counter32, Integer32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "IpAddress", "Gauge32", "Counter64", "iso", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "TimeTicks", "Counter32", "Integer32", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mcafee = ModuleIdentity((1, 3, 6, 1, 4, 1, 1230))
mcafee.setRevisions(('2006-09-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mcafee.setRevisionsDescriptions(('Initial Definition',))
if mibBuilder.loadTexts: mcafee.setLastUpdated('200607110000Z')
if mibBuilder.loadTexts: mcafee.setOrganization('McAfee, Inc.')
if mibBuilder.loadTexts: mcafee.setContactInfo('McAfee Customer Service Department\n\n                         Postal: 5000 Headquarters Drive\n                         Plano, TX  75024\n                         USA\n\n                         Tel: +1 800 338 8754\n\n                         E-mail: support@mcafee.com')
if mibBuilder.loadTexts: mcafee.setDescription(' The Structure of Management Information for the\n\t\t  McAfee enterprise.')
mcafeeGATEWAY = ObjectIdentity((1, 3, 6, 1, 4, 1, 1230, 2))
if mibBuilder.loadTexts: mcafeeGATEWAY.setStatus('current')
if mibBuilder.loadTexts: mcafeeGATEWAY.setDescription('McAfee Gateway Products')
mibBuilder.exportSymbols("MCAFEE-SMI", mcafee=mcafee, mcafeeGATEWAY=mcafeeGATEWAY, PYSNMP_MODULE_ID=mcafee)
