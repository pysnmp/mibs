#
# PySNMP MIB module MCAFEE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-SMI
# Produced by pysmi-1.1.8 at Mon Jan  9 13:42:33 2023
# On host fv-az210-608 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Counter32, Gauge32, Integer32, TimeTicks, NotificationType, Unsigned32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, ModuleIdentity, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "Gauge32", "Integer32", "TimeTicks", "NotificationType", "Unsigned32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "ModuleIdentity", "ObjectIdentity", "Counter64")
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
mibBuilder.exportSymbols("MCAFEE-SMI", mcafee=mcafee, PYSNMP_MODULE_ID=mcafee, mcafeeGATEWAY=mcafeeGATEWAY)
