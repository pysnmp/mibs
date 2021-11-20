#
# PySNMP MIB module MCAFEE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-SMI
# Produced by pysmi-1.1.3 at Sat Nov 20 21:26:20 2021
# On host fv-az121-977 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Bits, TimeTicks, Counter32, NotificationType, ObjectIdentity, MibIdentifier, enterprises, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Bits", "TimeTicks", "Counter32", "NotificationType", "ObjectIdentity", "MibIdentifier", "enterprises", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Counter64")
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
mibBuilder.exportSymbols("MCAFEE-SMI", mcafeeGATEWAY=mcafeeGATEWAY, PYSNMP_MODULE_ID=mcafee, mcafee=mcafee)
