#
# PySNMP MIB module ADTRAN-AOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS
# Produced by pysmi-1.1.8 at Thu Apr 27 09:09:13 2023
# On host fv-az247-870 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
adIdentityShared, adShared = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared", "adShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Integer32, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, ModuleIdentity, NotificationType, TimeTicks, MibIdentifier, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Integer32", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "ModuleIdentity", "NotificationType", "TimeTicks", "MibIdentifier", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53))
adGenAOSMib.setRevisions(('2014-09-10 00:00', '2012-04-27 00:00', '2010-07-05 00:00', '2004-10-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSMib.setRevisionsDescriptions(('Added adGenAOSMef OID.', 'Added adGenAOSApplications OID.', 'Added adGenAOSPower OID.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: adGenAOSMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAOSMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSMib.setContactInfo('Technical Support Dept.\n                Postal: ADTRAN, Inc.\n                901 Explorer Blvd.\n                Huntsville, AL 35806\n\n                Tel: +1 800 726-8663\n                Fax: +1 256 963 6217\n                E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSMib.setDescription('This MIB defines the Adtran OS enterprise tree node.  It\n                         provides a basis for the definition of all other Adtran OS\n                         MIBs.')
adGenAOS = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53))
adGenAOSCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1))
adGenAOSRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 2))
adGenAOSSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 3))
adGenAOSSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4))
adGenAOSVoice = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5))
adGenAOSWan = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 6))
adGenAOSPower = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 7))
adGenAOSConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99))
adGenAOSApplications = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 8))
adGenAOSMef = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9))
mibBuilder.exportSymbols("ADTRAN-AOS", adGenAOSVoice=adGenAOSVoice, adGenAOSSecurity=adGenAOSSecurity, PYSNMP_MODULE_ID=adGenAOSMib, adGenAOSApplications=adGenAOSApplications, adGenAOS=adGenAOS, adGenAOSPower=adGenAOSPower, adGenAOSSwitch=adGenAOSSwitch, adGenAOSMib=adGenAOSMib, adGenAOSMef=adGenAOSMef, adGenAOSRouter=adGenAOSRouter, adGenAOSCommon=adGenAOSCommon, adGenAOSConformance=adGenAOSConformance, adGenAOSWan=adGenAOSWan)
