#
# PySNMP MIB module PRIV-VENDORDEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRIV-VENDORDEF-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:46:12 2022
# On host fv-az74-997 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, MibIdentifier, TimeTicks, Counter64, IpAddress, iso, Counter32, Unsigned32, Integer32, Gauge32, enterprises, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Counter64", "IpAddress", "iso", "Counter32", "Unsigned32", "Integer32", "Gauge32", "enterprises", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
privateVendorOID = ModuleIdentity((1, 3, 6, 1, 4, 1, 738))
privateVendorOID.setRevisions(('2007-09-29 00:00',))
if mibBuilder.loadTexts: privateVendorOID.setLastUpdated('200709290000Z')
if mibBuilder.loadTexts: privateVendorOID.setOrganization('BATM Advanced Communication')
mibBuilder.exportSymbols("PRIV-VENDORDEF-MIB", PYSNMP_MODULE_ID=privateVendorOID, privateVendorOID=privateVendorOID)
